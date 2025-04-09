from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import Chatbot

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to handle cross-origin requests (adjust as per your needs)
origins = [
    "http://localhost",  # Frontend running on localhost
    "http://localhost:8501",  # Streamlit frontend port (adjust accordingly)
    "https://your-frontend-url.com",  # Add any other frontend URLs you want to allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins to allow
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Instantiate the chatbot
chatbot = Chatbot()

# Pydantic model to parse incoming JSON request
class ChatRequest(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Igbo Chatbot API"}

@app.post("/chat")
def get_chat_response(request: ChatRequest):
    """
    Endpoint for chatting with the bot.
    :param request: The user input as a JSON payload.
    :return: Chatbot's response as a JSON.
    """
    try:
        query = request.user_input
        response = chatbot.get_response(query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}