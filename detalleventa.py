from product import Producto

class DetalleVenta:
    def __init__(self, producto: Producto, cantidad):
        self._producto= producto
        self._cantidad= cantidad

    @property
    def cantidad(self):
        return self._producto
    @property
    def subtotal(self):
        return self.precio * self._cantidad
    