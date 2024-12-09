from fastapi import FastAPI
from .routers import pizzas

app = FastAPI()
app.include_router(pizzas.router)

@app.get("/")
def read_root():
    """
    Racine de l'API
    """
    return {"message": "Pizzas API"}