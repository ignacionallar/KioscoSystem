from producto import Producto
from detalleventa import DetalleVenta
from venta import Venta

producto1= Producto("Gaseosa",3000,10)
producto2= Producto("Hielo",1000,5)

print(producto1.to_dict())
print(producto2.to_dict())

venta=Venta()
venta.agregar_detalleventa(producto1,3)
venta.agregar_detalleventa(producto2,4)
print(venta.to_dict())