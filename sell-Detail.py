class SellDetail:
    def __init__(self, id, sell_id, product_id, quantity, subtotal):
        if quantity <= 0:
            raise ValueError("la cantidad no deve ser cero")
        if subtotal <=0:
            raise ValueError ("el subtotal no puede ser negativo")
        
        self._id= id
        self._sell_id= sell_id
        self._product_id= product_id
        self._quantity= quantity
        self._subtotal= subtotal

    @property
    def id(self):
        return self._id
    
    @property
    def sell_id(self):
        return self._sell_id
    
    @property
    def product_id(self):
        return self._product_id
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity <=0:
            raise ValueError ("la cantidad no puede ser cero")
        self._quantity =new_quantity

    @property
    def subtotal(self):
        return self._subtotal