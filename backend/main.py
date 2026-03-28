from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the app
app = FastAPI()

# Create a data model for what the frontend will send you
class UserRequest(BaseModel):
    message: str

# 1. A simple health check route
@app.get("/")
def read_root():
    return {"status": "Backend is alive!"}

# 2. The route your frontend will call to talk to the AI
@app.post("/api/chat")
def chat_with_agent(request: UserRequest):
    user_message = request.message
    
    # LATER: This is where you will import and call your teammates' AI function
    # ai_response = my_teammates_ai_function(user_message)
    
    # For now, just echo it back so you can test the frontend connection
    return {"reply": f"AI says: I received '{user_message}'"}