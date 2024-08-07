from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma 
from langchain_community.embeddings import OllamaEmbeddings

#Load the pdf files and split them into chunks
file_path = "./MSOW.pdf"
loader = PyPDFLoader(file_path)

pages = loader.load_and_split()
# print(pages)
# for page in pages:
#     print(page)

# Setup Vector Db Chroma
vector_store = Chroma.from_documents(documents=pages, embedding=OllamaEmbeddings(model="llama3"))
answers = vector_store.similarity_search("WHo is the project manager from Meta")
for answer in answers:
    print(answer)
    