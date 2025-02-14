import os

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float

from pydantic import BaseModel

DB_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DB_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modèle de la table User


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, nullable=False, index=True, unique=True)
    password = Column(String, nullable=False)


class UserBase(BaseModel):
    email: str
    password: str


class UserCreateDTO(UserBase):
    """
    User sans id (utile pour la création)
    """
    pass


class UserSignInDTO(UserBase):
    """
    User sans id (utile pour la création)
    """
    pass


class User(UserBase):
    """
    User avec id
    """
    id: int

    class Config:
        from_attributes = True


Base.metadata.create_all(engine)
