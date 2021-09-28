from fastapi import Depends, APIRouter
from models import *

product_router = APIRouter()


@product_router.get('/{name_or_id}', response_model=ProductModel)
def get_product(name_or_id: IdOrName = Depends()):
    return {
        "id": 100,
        "name": "cat",
        "description": "fdf",
        "buying_price": 500,
        "selling_price": 600
    }
    # return main_inventory.get_product(name_or_id)


@product_router.delete('/{name_or_id}', response_model=None)
def remove_product(name_or_id: IdOrName = Depends()):
    # main_inventory.remove_product(name_or_id)
    ...


@product_router.put('/{name_or_id}', response_model=None)
def update_product(new_pro: UpdateProductModel, name_or_id):
    #     main_inventory.update_product(name_or_id, new_pro)
    ...
