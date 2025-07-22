from fastapi import FastAPI
from pydantic import BaseModel

# Data Models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# App
app = FastAPI()

# Routing
@app.post("/items/")
async def create_item(item: Item):
    return item