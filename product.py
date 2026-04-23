class Product:
    def __init__(self,name,price,stock):
        if price<0:
            raise ValueError("Precio negativo")
        
        self._name=name
        self._price=price
        self._stock=stock
        
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def stock(self):
        return self._stock
    
    @name.setter
    def name(self,new_name):
        self._name=new_name

    @price.setter
    def price(self,new_price):
        self._price=new_price

    @stock.setter
    def stock(self,new_stock):
        self._stock=new_stock