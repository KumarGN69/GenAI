from langchain_community.document_loaders import PyPDFLoader
file_path = "./MSOW.pdf"

loader = PyPDFLoader(file_path)

pages = loader.load_and_split()
# print(pages)
for page in pages:
    print(page)