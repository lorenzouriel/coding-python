from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/new_endpoint")
def read_new_endpoint():
    return {"Endpoint": "Example"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id * 2}


# http://127.0.0.1:8000/docs é o nosso client, ou seja, uma documentação da nossa API
# response = request.get("http://127.0.0.1:8000/")