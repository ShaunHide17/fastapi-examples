from fastapi import APIRouter, Path, Query
from pydantic import BaseModel
import random

# Data Models
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class RecommendationScore(BaseModel):
    basket_id: int
    user_affinity_score: float
    purchase_probability: float
    recommended_items: list[str]
    confidence_level: str
    model_version: str = "v2.1"

class Basket(BaseModel):
    user: str
    items: list[Item]
    total_price: float
    total_tax: float

# FastAPI Router
router = APIRouter(
    prefix="/scoring",
    tags=["scoring"],
    responses={404: {"description": "Basket not found"}},
)

# Routing
@router.get("/recommend/{basket_id}")
async def get_recommendation_score(
    basket_id: int = Path(..., ge=1, description="The basket ID to generate recommendations for"),
    include_items: bool = Query(True, description="Include recommended item list"),
    model_type: str = Query("collaborative", description="Recommendation model type")
) -> RecommendationScore:

    
    # Mock recommendation logic (in real app, this would call ML models)
    random.seed(basket_id)  # Consistent results for same basket_id
    
    # Simulate different scoring based on basket_id
    base_affinity = min(0.95, 0.3 + (basket_id % 10) * 0.07)
    purchase_prob = min(0.90, base_affinity * random.uniform(0.7, 1.2))
    
    # Mock recommended items based on "collaborative filtering"
    item_pool = [
        "Premium Wireless Headphones", "Smart Fitness Tracker", 
        "Eco-Friendly Water Bottle", "Bluetooth Speaker",
        "Laptop Stand", "Organic Coffee Beans", "LED Desk Lamp",
        "Wireless Charging Pad", "Ergonomic Mouse", "Plant-based Protein"
    ]
    
    num_recommendations = 3 if include_items else 0
    recommended_items = random.sample(item_pool, num_recommendations) if include_items else []
    
    # Determine confidence level
    if purchase_prob >= 0.8:
        confidence = "high"
    elif purchase_prob >= 0.5:
        confidence = "medium"
    else:
        confidence = "low"
    
    return RecommendationScore(
        basket_id=basket_id,
        user_affinity_score=round(base_affinity, 3),
        purchase_probability=round(purchase_prob, 3),
        recommended_items=recommended_items,
        confidence_level=confidence,
        model_version=f"v2.1-{model_type}"
    )