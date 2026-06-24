import os
import json
import tempfile
import shutil
import uuid
import chromadb
from http.server import HTTPServer, BaseHTTPRequestHandler
from email import message_from_bytes
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ------------- Models ---------------------------
llm = ChatMistralAI(model="mistral-small-2603")
embedding_model = MistralAIEmbeddings(model="mistral-embed")

# ------------- Global state ---------------------
vectorstore  = None
retriever    = None
db_ready     = False
current_db_path = None   # track which folder is active so we can clean old ones

# ------------- Prompt ---------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are a helpful AI assistant.
Use ONLY the provided context to answer the question.
If the answer is not present in the context, say: \"I could not find the answer in the document.\""""),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

# ------------- RAG function ---------------------
def run_rag(query: str) -> dict:
    docs    = retriever.invoke(query)
    context = "\n\n".join([d.page_content for d in docs])
    fp      = prompt.invoke({"context": context, "question": query})
    resp    = llm.invoke(fp)
    return {"answer": resp.content, "chunk_count": len(docs)}

# ------------- Ingest function ------------------
def ingest_file(filepath: str, filename: str) -> dict:
    global vectorstore, retriever, db_ready, current_db_path

    ext = os.path.splitext(filename)[1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(filepath)
    elif ext in (".txt", ".md"):
        loader = TextLoader(filepath, encoding="utf-8")
    elif ext in (".docx",):
        loader = Docx2txtLoader(filepath)
    else:
        return {"error": f"Unsupported file type: {ext}. Use PDF, TXT, MD, or DOCX."}

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks   = splitter.split_documents(docs)

    if not chunks:
        return {"error": "Could not extract any text from the file."}

    # Drop old vectorstore reference completely — do NOT call reset() as it
    # doesn't release the Rust file lock reliably
    vectorstore = None
    retriever   = None
    db_ready    = False

    # Delete old DB folder after dropping the reference
    old_path = current_db_path
    if old_path and os.path.exists(old_path):
        try:
            shutil.rmtree(old_path)
        except Exception as e:
            print(f"  Warning: could not delete old DB: {e}")

    # Use a fresh unique folder so no file-lock conflicts ever occur
    new_db_path = os.path.join(BASE_DIR, f"chroma_DB_{uuid.uuid4().hex[:8]}")
    current_db_path = new_db_path

    vs = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=new_db_path
    )

    vectorstore = vs
    retriever   = vs.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
    )
    db_ready = True

    return {"success": True, "chunks": len(chunks), "filename": filename}

# ------------- HTTP Handler ---------------------
class RAGHandler(BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        pass

    def do_GET(self):
        if self.path in ('/', '/index.html', '/rag_ui.html'):
            fp = os.path.join(BASE_DIR, 'rag_ui.html')
            try:
                with open(fp, 'rb') as f:
                    body = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(body))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'rag_ui.html not found')
        elif self.path == '/api/status':
            self._json(200, {"ready": db_ready})
        else:
            self.send_response(404)
            self.end_headers()

    def _parse_multipart(self):
        """Parse multipart/form-data without cgi module."""
        content_type = self.headers.get('Content-Type', '')
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        # Build a fake email message so email.message can parse multipart
        mime_body = b"Content-Type: " + content_type.encode() + b"\r\n\r\n" + body
        msg = message_from_bytes(mime_body)

        fields = {}
        for part in msg.get_payload():
            disposition = part.get("Content-Disposition", "")
            # Extract field name
            name = None
            fname = None
            for item in disposition.split(";"):
                item = item.strip()
                if item.startswith('name='):
                    name = item[5:].strip('"')
                if item.startswith('filename='):
                    fname = item[9:].strip('"')
            if name:
                fields[name] = {
                    "data": part.get_payload(decode=True),
                    "filename": fname
                }
        return fields

    def do_POST(self):
        if self.path == '/api/upload':
            content_type = self.headers.get('Content-Type', '')
            if 'multipart/form-data' not in content_type:
                self._json(400, {"error": "Expected multipart/form-data"})
                return
            try:
                fields = self._parse_multipart()
            except Exception as e:
                self._json(400, {"error": f"Could not parse upload: {e}"})
                return

            file_field = fields.get('file')
            if not file_field or not file_field['data']:
                self._json(400, {"error": "No file received"})
                return

            filename = file_field['filename'] or "upload.pdf"
            suffix   = os.path.splitext(filename)[1] or ".pdf"

            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            tmp.write(file_field['data'])
            tmp.close()
            try:
                result = ingest_file(tmp.name, filename)
            finally:
                os.unlink(tmp.name)
            self._json(200 if "success" in result else 400, result)

        elif self.path == '/api/chat':
            length  = int(self.headers.get('Content-Length', 0))
            payload = json.loads(self.rfile.read(length))
            query   = payload.get('query', '').strip()
            if not query:
                self._json(400, {"error": "Empty query"})
                return
            if not db_ready:
                self._json(400, {"error": "No document loaded yet. Please upload a file first."})
                return
            try:
                self._json(200, run_rag(query))
            except Exception as e:
                self._json(500, {"error": str(e)})
        else:
            self._json(404, {"error": "Not found"})

    def _json(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

# ------------- Entry point ----------------------
PORT = 8000
print("---------------------RAG SYSTEM CREATED---------------------")
print(f"  UI ready  ->  http://localhost:{PORT}")
print("  Press Ctrl+C to quit.\n")
HTTPServer(('', PORT), RAGHandler).serve_forever()