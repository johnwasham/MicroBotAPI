from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "apples": 5,
        "message": "How do you like them apples?",
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
