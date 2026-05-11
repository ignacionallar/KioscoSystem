from producto import Producto
from detalleventa import DetalleVenta
from venta import Venta
from producto_repositorio import ProductoRepositorio

producto1= Producto("Gaseosa",3000,10)
producto2= Producto("Hielo",1000,5)

print(producto1.to_dict())
print(producto2.to_dict())

venta=Venta()
venta.agregar_detalleventa(producto1,5)
venta.agregar_detalleventa(producto2,4)
print(venta.to_dict())

repo=ProductoRepositorio()
repo.insertar_producto(producto1)
repo.insertar_producto(producto2)

print("##########################################")

for producto in repo.get_todos_productos():
    print(producto.to_dict())

print("##########################################")

print("Stock para el producto de id 4")
stock_consultado = repo.get_stock_productos(4)
print(stock_consultado)
print("Eliminar producto id 10")


if repo.eliminar_producto(11):
    print("Producto eliminado con exito")
else:
    print("Error al eliminar producto")
    
for producto in repo.get_todos_productos():
    print(producto.to_dict())