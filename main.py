from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/{item_id}")
async def create_item(item_id: int, item: str):
    return {"item_id": item_id, "item": item}

@app.get("/rashed")
async def read_item():
    return {"Rashed"}
