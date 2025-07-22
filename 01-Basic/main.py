from fastapi import FastAPI

# App
app = FastAPI()

# Routing .get, .post, .put, .delete
@app.get("/")
async def index():
    return {"message": "Hello World"}