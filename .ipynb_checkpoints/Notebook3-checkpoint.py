from fastapi import FastAPI
from threading import Thread
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# Run Uvicorn in a background thread
Thread(target=run).start()
