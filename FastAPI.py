from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
    
app = FastAPI()



class Message(BaseModel):
    id: int
    text: str
    user: str  # Added user field

messages = []

@app.post("/send_message/")
async def send_message(msg: Message):
    messages.append(msg.dict())  # Store message
    return {"status": "Message received", "data": msg}
messages = [{"id": 1, "text": "Hello","user": "arya"}, {"id": 2, "text": "Hi there","user": "abc"}]

@app.get("/get_messages/")
async def get_messages():
    return messages

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5004)  # Changed port to 5002

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Ensure POST is included
    allow_headers=["*"],
)

