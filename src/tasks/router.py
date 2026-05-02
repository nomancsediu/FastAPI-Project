from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix="/tasks")

# Create a new task
@task_routes.post("/create")
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


# Get all tasks
@task_routes.get("/all_tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    return controller.get_all_tasks(db)


# Get one task by id 
@task_routes.get("/{task_id}")
def get_one_task(task_id:int, db: Session = Depends(get_db)):
    return controller.get_one_task(task_id, db)


@task_routes.put("/{task_id}")
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controller.update_task(task_id, body, db)

@task_routes.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)