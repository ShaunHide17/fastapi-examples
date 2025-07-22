from fastapi import APIRouter
from pydantic import BaseModel

# Data Models
class User(BaseModel):
    username: str
    role: str

# FastAPI Router
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not authenticated"}},
)

# Routing
@router.get("/users")
async def get_users():
    return {"users": ["user1", "user2", "user3"]}