import datetime as dt
from product import Product
from sellDetail import SellDetail

class Sell:
    def __init__(self):
        self._date= dt.datetime.now().isoformat()
        self._items=[]
        self._total=0

    def calculate_total(self):
        total=0
        for item in self._items:
            total=item.subtotal+total
        return total
    
    @property
    def total(self):
        self._total=self.calculate_total()
        return self._total
    
    @property
    def items(self):
        return self._items
    
    @total.setter
    def total(self,new_total):
        self._total=new_total

    @items.setter
    def items(self,new_items):
        self._items=new_items
        
    def add_item(self, producto: Product, cantidad):
        self._items.append(SellDetail(producto, cantidad))

    def to_dict(self):
        return {
            "total": self.total,
            "fecha": self._date
        }