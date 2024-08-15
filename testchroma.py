import chromadb


chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="test_collection")

collection.add(
    documents= [
        "This is a document about pineapples",
        "this is a document about oranges"
        ],
    ids=["id1","id2"]
)
query = input("Enter your query: ")
results = collection.query(query_texts=query,n_results=2,)
print(results)