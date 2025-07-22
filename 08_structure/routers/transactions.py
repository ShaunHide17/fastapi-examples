from fastapi import APIRouter
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

# FastAPI Router
router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

# Routing
@router.post("/basket/")
async def create_basket(basket: Basket):
    return basket

@router.post("/items/")
async def create_item(item: Item):
    return item