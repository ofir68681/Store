from fastapi import FastAPI

from endpoints.inventory_endpoints import inventory_router
from endpoints.product_endpoints import product_router
from endpoints.store_endpoints import store_router
from inventory import Inventory

app = FastAPI()
main_inventory = Inventory()
app.include_router(store_router, prefix="/store", tags=['Store'])
app.include_router(product_router, prefix="/store/product", tags=['Product'])
app.include_router(inventory_router, prefix="/store/inventory", tags=['Inventory'])

# @app.put("/test", response_model=List[TestResponseModel], tags=['test'])
# def my_endpoint(input: TestInputModel):
#     return {'jjj': 444}
