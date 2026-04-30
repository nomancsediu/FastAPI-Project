from fastapi import Depends, FastAPI
from src.utils.db import get_db, Base, engine

Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import Session
app = FastAPI(title="This is my Task Management Application")

@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    return {"message": "DB connected successfully"}