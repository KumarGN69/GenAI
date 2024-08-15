from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma 
from langchain_community.embeddings import OllamaEmbeddings
import chromadb
from chromadb import PersistentClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from uuid import uuid4


#Load the pdf files and split them into chunks
"""This whole section on loading the PDF file, creating embeddings and adding to vector DB needs to be redone"""
#-----------------------------------------------------------------------------#
file_path = "./MSOW.pdf"

# file_path = "./MOSAIC_SOW.pdf"
loader = PyPDFLoader(file_path)
pages = loader.load_and_split()
# print(pages)
for page in pages:
    print(page.page_content)

#create the chroma client and collection
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="test_collection")

# Initialize the Chroma persistent client
client = PersistentClient(path="./")
#collection = client.create_collection(name="test_collection")

# split the document into chunks using text_splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=10)
split_documents = text_splitter.split_documents(pages)

#create embedding function and embed the split text chucks into the collection with unique IDs
embedding_function = OllamaEmbeddings(model="llama3.1")
for doc in split_documents:
    embedding = embedding_function.embed_query(doc.page_content)
    collection.add(
        documents=[doc.page_content],
        embeddings=[embedding],
        ids=[str(uuid4())]
    )

# client.persist()

#create a vector store
vector_store= Chroma(client=chroma_client, collection_name=collection.name)
#query the vector store for similarity
while True:
    question = input("Enter you query: ")
    query_embedding = embedding_function.embed_query(question)
    answers = vector_store.similarity_search_by_vector(embedding=query_embedding,k=2)
    for answer in answers:
        print(answer)
    