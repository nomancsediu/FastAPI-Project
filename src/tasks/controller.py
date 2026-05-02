from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.tasks.models import TaskModel


def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()
    new_task = TaskModel(**data)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status": "Task created successfully", "data": new_task}


def get_all_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"status": "Success", "data": tasks}


def get_one_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"status": "Success", "data": one_task}


def update_task(task_id: int, body: TaskSchema, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    one_task.title = body.title
    one_task.description = body.description
    one_task.is_completed = body.is_completed

    db.commit()
    db.refresh(one_task)

    return {"status": "Task updated successfully", "data": one_task}

from fastapi import HTTPException

def delete_task(task_id: int, db: Session):
    one_task = db.get(TaskModel, task_id)

    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(one_task)
    db.commit()

    return {"status": "Task deleted successfully"}