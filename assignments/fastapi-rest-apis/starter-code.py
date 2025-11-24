"""
FastAPI Task Management API - Starter Code
Assignment: Building REST APIs with FastAPI

This starter code provides the basic structure for your FastAPI application.
Complete the TODOs to build a fully functional task management API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create a FastAPI application instance
app = FastAPI()

# TODO: Define a Task model using Pydantic
# The Task model should have the following fields:
# - id: int
# - title: str
# - description: str
# - completed: bool (default: False)
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


# In-memory storage for tasks (this will reset when the server restarts)
tasks_db: List[Task] = []


# TODO: Create a GET endpoint at the root path "/" that returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API!"}


# TODO: Implement a GET endpoint "/tasks" that returns all tasks
@app.get("/tasks")
def get_all_tasks():
    pass


# TODO: Implement a GET endpoint "/tasks/{task_id}" that returns a specific task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


# TODO: Implement a POST endpoint "/tasks" that creates a new task
@app.post("/tasks", status_code=201)
def create_task(task: Task):
    pass


# TODO: Implement a PUT endpoint "/tasks/{task_id}" that updates an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    pass


# TODO: Implement a DELETE endpoint "/tasks/{task_id}" that deletes a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass


# To run this application, use the following command in your terminal:
# uvicorn starter-code:app --reload
#
# Then visit:
# - http://localhost:8000 to see the welcome message
# - http://localhost:8000/docs to see the interactive API documentation
