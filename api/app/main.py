import os

from fastapi import FastAPI, HTTPException, Depends

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from typing import List

from .models.pizza import Pizza, PizzaCreateDTO, PizzaModel

DB_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DB_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """
    Racine de l'API
    """
    return {"message": "Pizzas API"}


@app.get("/pizzas", response_model=List[Pizza])
def get_pizzas(db: Session = Depends(get_db)):
    """
    Récupère la liste des pizzas
    """
    return db.query(PizzaModel).all()


@app.get("/pizzas/{pizza_id}",response_model=Pizza)
def get_pizza(pizza_id: int, db: Session = Depends(get_db)):
    """
    Récupère une pizza par son id
    """
    pizza = db.query(PizzaModel).filter(PizzaModel.id == pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza


@app.post("/pizzas", response_model=Pizza, status_code=201)
def create_pizza(pizza: PizzaCreateDTO, db: Session = Depends(get_db)):
    """
    Créé une nouvelle pizza
    """
    existing_pizza = db.query(PizzaModel).filter(
        PizzaModel.name == pizza.name).first()
    if existing_pizza:
        raise HTTPException(status_code=400, detail="Pizza already exists")
    new_pizza = PizzaModel(**pizza.model_dump())
    db.add(new_pizza)
    db.commit()
    db.refresh(new_pizza)
    return new_pizza


@app.put("/pizzas/{pizza_id}", response_model=Pizza)
def update_pizza(pizza_id: int, updated_pizza: Pizza, db: Session = Depends(get_db)):
    """
    Met à jour une pizza sélectionnée selon son id
    """
    pizza = db.query(PizzaModel).filter(PizzaModel.id == pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    for key, value in updated_pizza.model_dump().items():
        setattr(pizza, key, value)
    db.commit()
    db.refresh(pizza)
    return pizza


@app.delete("/pizzas/{pizza_id}", status_code=204)
def delete_pizza(pizza_id: int, db: Session = Depends(get_db)):
    """
    Supprime une pizza sélectionnée selon son id
    """
    pizza = db.query(PizzaModel).filter(PizzaModel.id == pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    db.delete(pizza)
    db.commit()
