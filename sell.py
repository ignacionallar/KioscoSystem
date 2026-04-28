import datetime as dt
from product import Product
from sellDetail import SellDetail

class Sell:
    def __init__(self):
        self._date= dt.datetime.now().isoformat()
        self._items=[]
        self._total=0

    def calculate_total(self):
        for item in item:
            self._total=item.subtotal+self._total
        return self._total
    
    @property
    def total(self):
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
        
    

