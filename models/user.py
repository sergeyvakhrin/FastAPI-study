from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    def greet(self) -> str:
        return f"Hello, my name is {self.name}!"


class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

