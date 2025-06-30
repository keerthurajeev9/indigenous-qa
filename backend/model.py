from sentence_transformers import SentenceTransformer
from transformers import pipeline

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
qa_model = pipeline("text-generation", model="microsoft/phi-2")

def get_answer(question, vector_store):
    chunks = vector_store.similarity_search(question, k=3)
    context = "\n".join([c.page_content for c in chunks])
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    result = qa_model(prompt, max_new_tokens=100)[0]["generated_text"]
    return result.split("Answer:")[-1].strip()
