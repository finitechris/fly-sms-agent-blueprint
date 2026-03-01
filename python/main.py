from fastapi import FastAPI, Request
import uvicorn
from agent import analyze_message

app = FastAPI()

@app.post("/message")
async def receive_message(request: Request):
    data = await request.json()
    message_text = data.get("message", "")

    result = analyze_message(message_text)

    if result["action"] == "silent":
        return {"status": "silent"}

    return {
        "status": "respond",
        "response": result["response"]
    }
@app.get("/test")
def test_message(message: str):
    result = analyze_message(message)

    if result["action"] == "silent":
        return {"status": "silent"}

    return {
        "status": "respond",
        "response": result["response"]
    }
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
