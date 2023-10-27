""" FastAPI backend """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.chat_service import ChatService

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

@app.post("/get_response")
def send_message(chat_history: list = None, ai_models: list = None):
    """ Get chat response """
    # Initialize chat service
    chat_service = ChatService(chat_history, ai_models)
    # Get the chat response
    return chat_service.get_chat_response()
