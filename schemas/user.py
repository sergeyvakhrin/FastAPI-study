from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int = Field(..., title="User ID", ge=1)
    name: str
    age: Optional[int] = Field(25, title="Age of the user", ge=0, description="Must be a positive integer")
    email: EmailStr
    hobbies: Optional[List[str]] = None

    def greet(self) -> str:
        return f"Hello, my name is {self.name}!"