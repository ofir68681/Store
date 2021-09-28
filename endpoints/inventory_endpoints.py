from typing import List
from fastapi import Depends, APIRouter
from models import *

inventory_router = APIRouter()


@inventory_router.get('', response_model=List[ProductAmountModel])
def check_inventory():
    return [ProductAmountModel(name='cat', id=100, amount=2)]


@inventory_router.put('', response_model=None)
def purchase_supply_product(amount: int, is_Purchased: bool, name_or_id: IdOrName = Depends()):
    ...
    # main_inventory.update_inventory(name_or_id, amount, is_Purchased)
