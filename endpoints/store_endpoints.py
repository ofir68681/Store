from fastapi import APIRouter
from models import *

store_router = APIRouter()


@store_router.post('', response_model=None)
def new_product(new_pro: CreateProductModel):
    ...
