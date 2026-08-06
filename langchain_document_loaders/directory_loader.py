# from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_document_loaders import directory_loader, pdf_loader
loader = directory_loader(
    path='books',
    glob='*.pdf',
    loader_cls=pdf_loader
)

# docs = loader.load()
docs = loader.lazy_load()
for document in docs:
    print(document.metadata)
