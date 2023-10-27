""" Chat services utilities """
import os
from enum import Enum
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import openai
from openai.error import OpenAIError

# Load environment variables
load_dotenv()

# Set OpenAI API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_KEY2")
openai.organization = os.getenv("OPENAI_ORG2")

# Set the initial prompt
INITIAL_PROMPT = [{"role": "system", "content" : """
        You are a PR Prophet, answering questions about public relations
        and marketing as if you were a prophet in the Bible.  It's meant
        to be a light a playful way for pr and marketing professionals to
        get advice about their craft.  Keep your answers brief almost like
        a two paragraph daily devotional."""}]

openai_models = ["gpt-4-0613", "gpt-4-0613", "gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-0613"]

class ChatRole(str, Enum):
    """ Chat role """
    AI = "assistant"
    USER = "user"

class ChatMessage(BaseModel):
    """ Chat message """
    message: str = Field(description = "Message content")
    role: ChatRole = Field(description = "Message role")

class ChatService:
    """ Chat services utilities """
    def __init__(self, chat_history: list = None, ai_models: list = None):
        """ Initialize chat history """
        self.chat_history = chat_history if chat_history else INITIAL_PROMPT
        self.openai_models = openai_models if openai_models else ai_models

    def get_chat_response(self) -> dict:
        """ Get chat response """
        # Append the user message to the chat history
        # Iterate through the models
        for model in self.openai_models:
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    messages= [{"role": m["role"], "content": m["content"]}
                                for m in self.chat_history],
                    temperature=1,
                    max_tokens=250,
                )
                ai_message = response.choices[0].message.content
                # Add the AI response to the chat history
                # Return the chat response
                return {"message": ai_message}
            except OpenAIError as e:
                print(f"OpenAI API error: {e}")
                continue
