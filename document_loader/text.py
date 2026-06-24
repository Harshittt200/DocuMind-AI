from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

spiltter=CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1

)

data=TextLoader("documentloader/notes.txt")
docs=data.load()
chunks=spiltter.split_documents(docs)

print(len(chunks))