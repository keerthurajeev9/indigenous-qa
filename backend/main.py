from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from model import get_answer
from utils import save_and_extract_text
from vector_store import load_vector_store

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_store = None

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    text = await save_and_extract_text(file)
    global vector_store
    vector_store = load_vector_store(text)
    return {"status": "Document uploaded and indexed."}

@app.post("/query/")
async def query(question: str = Form(...)):
    if not vector_store:
        return {"error": "No document uploaded."}
    answer = get_answer(question, vector_store)
    return {"answer": answer}
