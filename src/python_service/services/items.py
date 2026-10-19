from itertools import count

from python_service.models.items import Item
from python_service.schemas.items import ItemCreate

_items: dict[int, Item] = {}
_next_id = count(1)


def create_item(payload: ItemCreate) -> Item:
    item = Item(id=next(_next_id), name=payload.name)
    _items[item.id] = item
    return item


def get_item(item_id: int) -> Item | None:
    return _items.get(item_id)
