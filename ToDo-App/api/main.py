import json
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ToDo(BaseModel):
    id: int
    todo: str
    status: bool


def read() -> dict:
    with open("data.json") as f:
        return json.load(f)["todos"]

def write(data: ToDo):
    with open("data.json") as f:
        content = json.load(f)

    content["todos"].append(data.dict())

    with open("data.json", "w") as f:
        json.dump(content, f)


def update(id: int, data: ToDo):
    with open("data.json") as f:
        content = json.load(f)

    index = -1

    for i, e in enumerate(content["todos"]):
        if e["id"] == id:
            content["todos"][i].update(data.dict())
            index = i
            break
    else:
        raise HTTPException(404)

    print(content)

    with open("data.json", "w") as f:
        json.dump(content, f)

def delete(id: int):
    with open("data.json") as f:
        content = json.load(f)

    index = -1

    for i, e in enumerate(content["todos"]):
        if e["id"] == id:
            index = i
            break
    else:
        raise HTTPException(404)

    del content["todos"][index]

    with open("data.json", "w") as f:
        json.dump(content, f)


@app.get("/read")
def get():
    return read()


@app.post("/write")
def post(data: ToDo):
    write(data)
    for i in read():
        if i["id"] == data.id:
            return i

    raise HTTPException(500)

@app.put("/update/{id}")
def put(id: int, data: ToDo):
    update(id, data)
    for i in read():
        if i["id"] == data.id:
            return i

    raise HTTPException(500)


@app.delete("/delete/{id}")
def delet(id: int):
    delete(id)
    return {"Status": "Success"}
