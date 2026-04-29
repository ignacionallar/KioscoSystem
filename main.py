from product import Product
from sell import Sell
from sellDetail import SellDetail
from product_repository import ProductRepository

producto1= Product("Coca",2500,10)
producto2= Product("Papa",1000,10)
print(producto1.to_dict())

venta=Sell()
venta.add_item(producto1,3)
venta.add_item(producto2,2)
print(venta.to_dict())

repo=ProductRepository()
repo.insert_product(producto1)
repo.insert_product(producto2)

print("##############################################")
for producto in repo.get_all_products():
    print(producto.to_dict())
print("##############################################")
