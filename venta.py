import datetime as dt
from product import Producto
from detalleventa import DetalleVenta

class Venta():
    def __init__(self):
        self._date= dt.datetime.now().isoformat()
        self._producto=[]
    @property
    def total(self):
        total= 0
        for detalleventa in self._producto:
            total+=self._subtotal
        return total
    def agregar_detalleventa(self, producto: Producto, cantidad):
        self._detalleventa.append(DetalleVenta(producto, cantidad))

    def to_dict(self):
        return{
            "total": self._total,
            "fecha": self._date
        }       