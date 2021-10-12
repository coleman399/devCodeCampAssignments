from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()
    
    def add_item_to_shopping_cart(self, item):
        self.shopping_cart.add_item_to_cart(item)

    def show_items_in_shopping_cart(self):
        for self.items in range(self.shopping_cart.number_of_products()):
            self.item_from_cart = self.shopping_cart.shopping_cart[self.items]
            print(f"Product: {self.item_from_cart}")
