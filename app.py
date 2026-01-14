from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="Cloud-Native Student Task Management System")

tasks_db = {}

class TaskCreate(BaseModel):
    title: str
    description: str | None = ""

class TaskUpdate(BaseModel):
    status: str

class Task(BaseModel):
    task_id: str
    title: str
    description: str
    status: str
    created_at: str

def validate_status(status: str):
    if status not in ["Pending", "In Progress", "Completed"]:
        raise HTTPException(status_code=400, detail="Invalid status value")

@app.post("/task", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    task_id = str(uuid4())
    new_task = {
        "task_id": task_id,
        "title": task.title,
        "description": task.description or "",
        "status": "Pending",
        "created_at": datetime.utcnow().isoformat()
    }
    tasks_db[task_id] = new_task
    return new_task

@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return list(tasks_db.values())

@app.get("/task/{task_id}", response_model=Task)
def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/task/{task_id}")
def update_task(task_id: str, data: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    validate_status(data.status)
    tasks_db[task_id]["status"] = data.status
    return {"message": "Task updated successfully"}

@app.delete("/task/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": "Task deleted successfully"}