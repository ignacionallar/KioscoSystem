class Product:
    def __init__(self,name,price,stock):
        if name == "":
            raise ValueError("Nombre vacio")
        if price<0:
            raise ValueError("Precio negativo")
        if stock<=0:
            raise ValueError("Stock invalido")
        
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
        if new_name == "":
            raise ValueError("Nombre vacio")
        else:
            self._name=new_name

    @price.setter
    def price(self,new_price):
        if new_price < 0:
            raise ValueError("Precio negativo")
        else:  
            self._price=new_price

    @stock.setter
    def stock(self,new_stock):
        if new_stock <= 0:
            raise ValueError("Stock invalido")
        else:
            self._stock=new_stock
    
    def to_dict(self):
        return{
            "name":self._name,
            "price":self._price,
            "stock":self._stock
        }