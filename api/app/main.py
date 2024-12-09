from typing import Union

from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import os
import time

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')


def wait_for_db(db_uri):
    """checks if database connection is established"""

    _local_engine = create_engine(db_uri)

    _LocalSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=_local_engine
    )

    up = False
    while not up:
        try:
            # Try to create session to check if DB is awake
            db_session = _LocalSessionLocal()
            # try some basic query
            db_session.execute("SELECT 1")
            db_session.commit()
        except Exception as err:
            print(f"Connection error: {err}")
            up = False
        else:
            up = True

        time.sleep(2)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Test Fast API"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items")
def read_items():
    return []
