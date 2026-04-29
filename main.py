from product import Product
from sell import Sell
from sellDetail import SellDetail

producto1= Product("Coca",2500,10)
producto2= Product("Papa",1000,10)
print(producto1.to_dict())

detalleVenta1= SellDetail(producto1,5)
print(detalleVenta1.to_dict())

venta=Sell()
venta.add_item(producto1,3)
venta.add_item(producto2,2)
print(venta.to_dict())