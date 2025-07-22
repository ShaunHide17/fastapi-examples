from fastapi import FastAPI, Depends

from .dependencies import get_query_token, get_token_header
from .routers import transactions
from .routers import scoring

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(transactions.router)
app.include_router(scoring.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}