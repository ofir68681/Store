from pydantic import BaseModel
from typing import Optional, Union


class CreateProductModel(BaseModel):
    name: str
    description: str
    buying_price: float
    selling_price: float


class UpdateProductModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    buying_price: Optional[float]
    selling_price: Optional[float]


class ProductModel(CreateProductModel):
    id: int


class ProductAmountModel(BaseModel):
    id: int
    name: Optional[str]
    amount: int


class IdOrName(BaseModel):
    name_or_id: Union[int, str]


# class TestInputModel(BaseModel):
#     name: str
#     age: int
#
#
# class TestResponseModel(BaseModel):
#     kaki: str
#     cat: int
