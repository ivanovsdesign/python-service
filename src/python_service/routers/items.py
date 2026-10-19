from fastapi import APIRouter, HTTPException

from python_service.schemas.items import ItemCreate, ItemRead
from python_service.services import items as item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", response_model=ItemRead, status_code=201)
def create_item(payload: ItemCreate):
    return item_service.create_item(payload)


@router.get("/{item_id}", response_model=ItemRead)
def read_item(item_id: int):
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
