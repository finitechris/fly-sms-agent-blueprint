from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/message")
async def receive_message(request: Request):
    data = await request.json()
    print("Incoming message:", data)

    # Placeholder response
    return {"status": "received", "action": "silent"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
