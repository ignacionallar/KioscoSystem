from product import Product
class SellDetail:
    def __init__(self, product: Product, quantity):
        self._product= product
        self._quantity= quantity
        self._subtotal=0

    @property
    def product(self):
        return self._product
    
    @property
    def quantity(self):
        return self._quantity
    
    @product.setter
    def product(self, new_product: Product):
        self._product= new_product

    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity= new_quantity

    def calculate_subtotal(self):
        self._subtotal=self._product.price * self._quantity
        return self._subtotal
    