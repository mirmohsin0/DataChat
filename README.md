# 💬 DataChat

A modern full-stack chat logging system built with FastAPI and a dynamic frontend UI.  
Send, store, and search messages with a clean, interactive interface.

---

## 🚀 Features

- ✉️ Send messages instantly
- 📜 View complete chat history
- 🔍 Search messages by username
- 🔎 Search messages by keyword
- 🎨 Modern UI (CSS)
- ⚡ Fast API responses using FastAPI

---

## 🧠 Tech Stack

- **Backend:** FastAPI  
- **Frontend:** HTML, CSS, JavaScript  
- **Storage:** JSON file  

---

## 📂 Project Structure
backend.py        → Core business logic
main.py           → FastAPI routes (API layer)
index.html        → Frontend UI
chat_data.json    → Data storage
README.md         → Project documentation


## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
http://127.0.0.1:8000/docs


