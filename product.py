class Producto:
    def __init__(self,name,price,stock):
        if price<0:
            raise ValueError("Precio negativo")
        
        self.name=name
        self.price=price
        self.stock=stock
        