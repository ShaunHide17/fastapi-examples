from fastapi import FastAPI
from pydantic import BaseModel

# Data Models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Basket(BaseModel):
    user: str
    items: list[Item]
    total_price: float
    total_tax: float

# App
app = FastAPI()

# Routing
@app.post("/basket/")
async def create_basket(basket: Basket):
    return basket

@app.post("/items/")
async def create_item(item: Item):
    return item