from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()



class Message(BaseModel):
    text: str
    user: str

messages = []

@app.post("/send_message/")
async def send_message(msg: Message):
    messages.append(msg.dict())  # Store message
    return {"status": "Message received"}
messages = [{"id": 1, "text": "Hello"}, {"id": 2, "text": "Hi there"}]

@app.get("/get_messages/")
async def get_messages():
    return messages

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5004)  # Changed port to 5002

