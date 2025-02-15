from fastapi import FastAPI

from routers import item, user
from services.user_service import foo_1, foo_2

app = FastAPI()

app.include_router(item.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return {'message': 'Hello, World!'}


@app.get("/hello/{name}")
def read_hellow(name):
    return {'message': f'Hello, {name}!'}


foo_1()
foo_2()
