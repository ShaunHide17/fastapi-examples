from fastapi import FastAPI

# App
app = FastAPI()

# Routing
@app.get("/item/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def get_items(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id, "q": "No query string"} 

