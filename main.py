from fastapi import Depends, FastAPI
from src.utils.db import get_db, Base, engine
from src.tasks.models import TaskModel
from src.tasks.router import task_routes
from src.user.router import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="This is my Task Management Application")
app.include_router(task_routes)
app.include_router(user_routes)

