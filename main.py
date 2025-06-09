from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/profile")
def profile(data: dict):
    return {"msg": "登録しました"}

@app.get("/restaurants")
def restaurants():
    return [
        {"id": 1, "name": "ダミー寿司", "capacity": 12},
        {"id": 2, "name": "モック焼肉", "capacity": 30},
    ]

@app.post("/ask-ai")
def ask_ai(q: Question):
    return {"reply": f"AI応答: {q.text}"}
