from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import firestore

app = FastAPI()
db = firestore.Client()

# 店舗検索
@app.get("/search")
def search(keyword: str = ""):
    return [
        {"id": 1, "name": "ダミー寿司", "capacity": 12},
        {"id": 2, "name": "モック焼肉", "capacity": 30}
    ]







# プロフィール登録
class UserProfile(BaseModel):
    user_id: str
    name: str

@app.post("/profile")
def profile(profile: UserProfile):
    return {"msg": f"登録しました: {profile.user_id}"}

# AI質問スタブ
class Question(BaseModel):
    text: str

@app.post("/ask-ai")
def ask_ai(q: Question):
    return {"reply": f"AI応答: {q.text}"}

# ヘルスチェック
@app.get("/health")
def health():
    return {"status": "ok"}

# 推薦ダミー
@app.get("/recommend")
def recommend_restaurants(user_id: str = ""):
    return [
        {"id": 2, "name": "モック焼肉", "capacity": 30}
    ]

# レビュー分析スタブ
@app.get("/analyze")
def analyze_review(review: str = ""):
    return {"analysis": f"入力されたレビュー：{review}（分析結果ダミー）"}



