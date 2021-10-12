from shopping_cart import ShoppingCart
from product import Product
from customer import Customer
from alarm_clock import AlarmClock

alarm_clock = AlarmClock()
shopping_cart = ShoppingCart()
product1 = Product("Hair Straightener", 55.00, "Beauty")
product2 = Product("Hair Spray", 15.00, "Beauty")
product3 = Product("Head Phones", 74.00, "Electionics")
customer = Customer(input("Please enter your name: "))

alarm_clock.set_time("10:45")

alarm_clock.set_time(input("please input new time: "))

alarm_clock.set_alarm_on_or_off(True)

alarm_clock.set_alarm_time(input("please provide alarm time: "))

print(customer.name)

customer.add_item_to_shopping_cart(product1)
customer.add_item_to_shopping_cart(product2)
customer.add_item_to_shopping_cart(product3)

customer.show_items_in_shopping_cart()

print(f"Total number of products: {customer.shopping_cart.number_of_products()}")

customer.shopping_cart.empty_items_in_cart()

print(f"Item in shopping cart: {customer.show_items_in_shopping_cart()}")

print(f"Total number of products: {shopping_cart.number_of_products()}")
