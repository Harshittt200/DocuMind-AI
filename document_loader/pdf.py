from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data=PyPDFLoader("documentloader/GRU.pdf")
docs=data.load()

splitter=TokenTextSplitter(
    chunk_size=1000,
    chunk_overlap=1
)
chunks=splitter.split_documents(docs)
print(len(chunks))