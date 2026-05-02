from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.tasks.models import TaskModel


# Create a new task
def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(**data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# Get all tasks
def get_all_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks


# Get one task by id
def get_one_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return one_task



# Update a task by id
def update_task(task_id: int, body: TaskSchema, db: Session):
    one_task = db.get(TaskModel, task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    one_task.title = body.title
    one_task.description = body.description
    one_task.is_completed = body.is_completed

    db.commit()
    db.refresh(one_task)
    return one_task


# Delete a task by id
def delete_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(one_task)
    db.commit()
    return one_task
