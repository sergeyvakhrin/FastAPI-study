from typing import List
from fastapi import HTTPException, APIRouter
from models.user import User


router = APIRouter()


users = []
@router.post("/users/", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user


@router.get("/users/", response_model=List[User])
async def get_users():
    return users


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
        raise HTTPException(status_code=404, detail="User not found")
