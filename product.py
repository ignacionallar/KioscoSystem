class Producto:
    def __init__(self, nombre, precio, stock):
        if precio<0:
            raise ValueError("El precio no debe ser negativo.")
        if stock>=0:
            raise ValueError("El stock no debe ser negativo.")
        self._nombre= nombre
        self._precio= precio
        self._stock= stock
    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def stock(self):
        return self._stock
    
    nombre.setter
    def nombre(self,valor):
        if len(valor)>0:
            self._nombre=valor
            
    precio.setter
    def precio(self,valor):
        if valor > 0:
            self._precio= valor
        else:
            raise ValueError("El precio no debe ser negativo.")    
    
    stock.setter
    def stock(self,valor):
        if valor > 0:
            self._stock= valor
        else:
            raise ValueError("El Stock no debe ser negativo.")
    
    def to_dict(self):
        return{
            "Nombre": self._nombre,
            "Precio": self._precio,
            "Stock": self._stock
        }