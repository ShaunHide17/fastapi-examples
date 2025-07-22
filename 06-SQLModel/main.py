from fastapi import FastAPI
from models import Item, Basket

# App
app = FastAPI()

# Routing
@app.post("/basket/")
async def create_basket(basket: Basket):
    return basket

@app.post("/items/")
async def create_item(item: Item):
    return item