from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ValidationError
from starlette.exceptions import HTTPException

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    id: int = Field(..., title="User ID", ge=1)
    name: str
    age: Optional[int] = Field(25, title="Age of the user", ge=0, description="Must be a positive integer")
    email: EmailStr
    hobbies: Optional[List[str]] = None

    def greet(self) -> str:
        return f"Hello, my name is {self.name}!"


@app.post("/item/")
async def create_item(item: Item):
    return {"item": item}


@app.get("/")
def read_root():
    return {'message': 'Hello, World!'}


@app.get("/hello/{name}")
def read_hellow(name):
    return {'message': f'Hello, {name}!'}


users = []
@app.post("/users/", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user


@app.get("/users/", response_model=List[User])
async def get_users():
    return users


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
        raise HTTPException(status_code=404, detail="User not found")


user1 = User(id=1, name="Alice", email="alice@example.com")
print(user1)
print(user1.greet())


try:
    user2 = User(id=-1, name="Bob", email="invalid-email", age=-5)
except ValidationError as e:
    print(e.json())

