from fastapi import FastAPI
from .routers import pizzas
from .routers import users

app = FastAPI()
app.include_router(pizzas.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    """
    Racine de l'API
    """
    return {"message": "Pizzas API"}
