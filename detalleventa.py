from producto import Producto

class DetalleVenta:
    def __init__(self, producto: Producto, cantidad):
        self._producto= producto
        self._cantidad= cantidad
        self._subtotal=0

    @property
    def producto(self):
        return self._producto
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def subtotal(self):
        return self.producto.precio * self._cantidad
    
    @producto.setter
    def producto(self, nuevo_producto: Producto):
        self._producto= nuevo_producto

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad= nueva_cantidad

    @subtotal.setter
    def subtotal (self, nuevo_subtotal):
        self._subtotal= nuevo_subtotal

    def to_dict(self):
        return{
            "Nombre": self._producto.nombre,
            "Cantidad": self._cantidad,
            "Subtotal": self.subtotal
        }