import datetime as dt
from product import Product
from sellDetail import SellDetail

class Sell:
    def __init__(self):
        self._date= dt.datetime.now().isoformat()
        self._items=[]

