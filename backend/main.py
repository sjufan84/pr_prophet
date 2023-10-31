""" FastAPI backend """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.chat_service import get_chat_response
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173",  # Make sure this matches your frontend port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """ Root endpoint """
    return {"message": "Hello, World!"}

class ChatHistory(BaseModel):
    chat_history: list

@app.post('/get_response')
async def get_response(chat: ChatHistory = None):
    """ Get chat response """
    chat_history = chat.chat_history if chat else []
    response = get_chat_response(chat_history)
    return response