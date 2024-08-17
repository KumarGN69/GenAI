**ALL ITEMS IN BOLD AND OPEN and INCOMPLETE**
main.py
- UI using Gradio for inputs and response
- Invoke local llm via Ollama API call
- **restructure the file using read file classes and Search API classes**
- **Change the UI to give user the option to either read from pdf files or do an extrnal search to get latest information**
read_files.py
- Load pdf file via pdf loaders
- split via text splitter into smaller chunks
- Create embeddings and define a collection
- add the text chunks into the embedding collection
**- Create persistent collection?**
- Create a vector data store reference
- create an embedding for the query
- query the embedding collection using the embedded query using similarity search
- **use the results from the similarity search for the llm query/action?**
- **Restructure the code into classes and methods?**

search.py
- Use Tavily API to get the latest info for the query from external sources
- **Create embeddings and persistance into a vector DB?**

**Separation of Concerns using MVC design approach
- main - Control flow
- User Interface
- Query/search 
- Model for embedding and data store/persistence**
- 
