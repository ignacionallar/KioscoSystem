class Producto:
    def __init__(self, nombre, precio, stock,id=None):
        if len(nombre)==0:
            raise ValueError("Nombre Vacio")
        if precio<0:
            raise ValueError("El precio no debe ser negativo.")
        if stock<=0:
            raise ValueError("El stock no debe ser negativo.")
        
        self._nombre= nombre
        self._precio= precio
        self._stock= stock
        self._id=id
    
    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def stock(self):
        return self._stock
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if len(nuevo_nombre)==0:
            raise ValueError("Nombre en Vacio")
        else:    
            self._nombre=nuevo_nombre
            
    @precio.setter
    def precio(self,nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no debe ser negativo.") 
        else:
            self._precio= nuevo_precio

    @stock.setter
    def stock(self,nuevo_stock):
        if nuevo_stock < 0:
            raise ValueError("El Stock no debe ser negativo.")
        else:
            self._stock= nuevo_stock
    
    def to_dict(self):
        return{
            "Nombre": self._nombre,
            "Precio": self._precio,
            "Stock": self._stock,
            "Id": self._id
        }