from task1.rag import RAGPipeline

rag = RAGPipeline("data.pdf")

chunks300 = rag.chunk_documents(300, 50)
vector_store300 = rag.create_vector_store(chunks300)

rag.retrieve_chunks(
    vector_store300,
    "What is class?"
)
chunks700 = rag.chunk_documents(700, 50)
vector_store700 = rag.create_vector_store(chunks700)
rag.retrieve_chunks(
    vector_store700,
    "What is class?"
)
from task1.rag import RAGPipeline

rag = RAGPipeline("data.pdf")

chunks300 = rag.chunk_documents(300, 50)
vector300 = rag.create_vector_store(chunks300)

question = "What is class?"

docs = rag.retrieve_chunks(vector300, question)

answer = rag.generate_answer(docs, question)

print("\n================ FINAL ANSWER ================\n")
print(answer)