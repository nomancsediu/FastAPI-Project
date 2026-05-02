from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.tasks.models import TaskModel

def create_task(body: TaskSchema, db: Session):

    data = body.model_dump()
    new_task = TaskModel(title=data["title"],description=data["description"],is_completed=data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status": "Task created successfully", "data": new_task}


def get_all_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"status": "Success", "data": tasks}


def get_one_task(task_id:int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(status_code=404, detail="Task not found")
    else:
        return {"status": "Success", "data": one_task}



