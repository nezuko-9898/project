# main.py
from fastapi import FastAPI

app = FastAPI()  # Create FastAPI instance

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Example: Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}
