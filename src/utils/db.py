from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from websockets import connect

from src.utils.settings import settings
Base = declarative_base()

engine = create_engine(url=settings.DB_CONNECTION, echo=True)

LocalSession = sessionmaker(bind=engine)

def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()