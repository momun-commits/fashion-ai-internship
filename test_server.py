from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "test"}

import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)