class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []
    
    def number_of_products(self):
        self.total_products = len(self.shopping_cart)
        return self.total_products

    def add_item_to_cart(self, item):
        self.shopping_cart.append(item)

    def empty_items_in_cart(self):
        self.shopping_cart.clear()

