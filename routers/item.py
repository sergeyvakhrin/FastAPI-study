from fastapi import APIRouter
from schemas.item import Item


router = APIRouter()


@router.post("/item/")
async def create_item(item: Item):
    return {"item": item}
