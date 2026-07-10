from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
class RAGPipeline:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.documents = self.load_documents()
    def load_documents(self):
        print("Loading PDF...")
        reader = PdfReader(self.pdf_path)
        documents = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:   
                documents.append(
                    Document(
                        page_content=text,
                        metadata={"page": i + 1}
                    )
                )
        print(f"Loaded {len(documents)} pages")
        return documents
    def chunk_documents(self, chunk_size, chunk_overlap):
        print(f"\nChunking with size={chunk_size}")
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        chunks = splitter.split_documents(self.documents)
        print(f"Created {len(chunks)} chunks")
        return chunks
    def create_vector_store(self, chunks):
        print("\nLoading Embedding Model...")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Embedding all chunks...")
        vector_store = FAISS.from_documents(
        chunks,
        embeddings
        )

        print("FAISS Vector Store Created Successfully!")
        return vector_store
    
    def retrieve_chunks(self, vector_store, query, k=3):
        print("\nUser Question:")
        print(query)

        print("\nSearching in FAISS...")

        docs = vector_store.similarity_search(
        query,
        k=k
        )

        print(f"\nRetrieved {len(docs)} chunks:\n")

        for i, doc in enumerate(docs, start=1):

            print(f"----------- Chunk {i} -----------")
            print(doc.page_content[:400])
            print()

        return docs
    def generate_answer(self, docs, question):
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are a helpful AI assistant.

        Answer ONLY using the context provided below.
        If the answer is not present in the context, reply:
        "I don't know based on the provided document."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        print("\nGenerating answer using Llama 3.2...\n")

        llm = OllamaLLM(model="llama3.2")

        answer = llm.invoke(prompt)

        return answer