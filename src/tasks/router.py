from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List


task_routes = APIRouter(prefix="/tasks")


# Create a new task
@task_routes.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


# Get all tasks
@task_routes.get("/all_tasks", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db: Session = Depends(get_db)):
    return controller.get_all_tasks(db)


# Get one task by id
@task_routes.get("/get_one_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_one_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_one_task(task_id, db)


# Update a task by id
@task_routes.put("/update_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controller.update_task(task_id, body, db)


# Delete a task by id
@task_routes.delete("/delete_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)

