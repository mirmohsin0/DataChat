from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  

from backend import add_message, get_all_messages, search_user, search_keyword

app = FastAPI()

# ✅ ADD ONLY ONCE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/messages")
def messages():
    return get_all_messages()

@app.post("/send")
def send(username: str, message: str):
    return add_message(username, message)

@app.get("/search/user")
def search_by_user(username: str):
    return search_user(username)

@app.get("/search/keyword")
def search_by_keyword(keyword: str):
    return search_keyword(keyword)