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
        x=self.product.price * self._quantity
        return x
    
    @property
    def subtotal(self):
        self._subtotal=self.calculate_subtotal()
        return self._subtotal
    
    @subtotal.setter
    def subtotal(self, new_subtotal):
        self._subtotal=new_subtotal

    def to_dict(self):
        return {
            "name":self._product.name,
            "quantity":self._quantity,
            "subtotal":self.subtotal
        }
    