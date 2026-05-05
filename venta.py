import datetime as dt
from producto import Producto
from detalleventa import DetalleVenta

class Venta():
    def __init__(self):
        self._date= dt.datetime.now().isoformat()
        self._productos=[]
        self._total=0

    @property
    def total(self):
        total= 0
        for producto in self._productos:
            self._total+=producto.subtotal
        return self._total
    
    @property
    def productos(self):
        return self._productos
    
    @total.setter
    def total(self,nuevo_total):
        self._total= nuevo_total

    @productos.setter
    def productos(self, nuevo_producto):
        self._productos= nuevo_producto

    def agregar_detalleventa(self, producto: Producto, cantidad):
        self._productos.append(DetalleVenta(producto, cantidad))

    def to_dict(self):
        return{
            "total": self.total,
            "fecha": self._date
        }