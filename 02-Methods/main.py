from fastapi import FastAPI, Request

# App
app = FastAPI()

# Routing
@app.get("/")
@app.post("/")
def index(request: Request):
    if request.method == "GET":
        return {"message": "This is a GET request"}
    else:
        return {"message": "This is a POST request"}
