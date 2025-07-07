from fastapi import FastAPI, Body, Query, HTTPException
from typing import Optional

app = FastAPI()

dogs = {
    1: { "name": "ash", "age": 5 },
    2: { "name": "bub", "age": 6 },
    3: { "name": "coo", "age": 4 }
}

@app.get("/")
def welcome():
    return "hello world"

@app.get("/dogs")
def get_dogs(name: Optional[str] = Query(None)):
    if name is None:
        return dogs
    for id in dogs:
        if dogs[id]["name"] == name:
            return dogs[id]
    raise HTTPException(status_code = 404, detail = "name not found")

@app.get("/dogs/{id}")
def get_dog(id: int):
    if id in dogs:
        return dogs[id]
    raise HTTPException(status_code = 404, detail = "id not found")

@app.post("/dogs")
def post_dog(payload: dict = Body(...)):
    id   = payload["id"]
    name = payload["name"]
    age  = payload["age"]

    if id is not None:
        dogs[id] = { "name": name, "age": age }
        return { id: dogs[id] }
    raise HTTPException(status_code = 401, detail = "id must not be None")