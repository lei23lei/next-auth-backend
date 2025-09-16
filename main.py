from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import models
from pydantic import BaseModel
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/users")
async def get_users():
    return {"message": "Hello World"}

@app.post("/api/users")
async def create_user():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
