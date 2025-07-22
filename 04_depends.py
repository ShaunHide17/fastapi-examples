from fastapi import FastAPI, Query, Depends

# Depends
def pagination_params(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    return {"limit": limit, "offset": offset}

# App
app = FastAPI()

# Routing
@app.get("/items/")
async def get_items(pagination: dict = Depends(pagination_params)):
    return pagination

