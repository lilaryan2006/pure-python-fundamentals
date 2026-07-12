"""
Exercise 1: The E-Commerce Shopping Cart
 Your Task
       Create a Product class:
          Attributes: name (string), price (float), and stock (integer).
          Method: display_info() to print the product's details nicely.
       Create a ShoppingCart class:
          Attribute: items (a list to hold product objects).
          Method: add_item(product, quantity) — Adds a product to the cart only if there is enough stock. Remember to reduce the product's stock!
          Method: calculate_total() — Calculates and returns the total price of everything in the cart.
          Method: checkout() — Prints a receipt and clears the cart.
"""

from sympy import product


class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return self.name

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
        else:
            print("Not enough stock available.")

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total = total + product.price * quantity
        return total

    def checkout(self):
        print("Receipt:")
        for product, quantity in self.items:
            print(f"{product.name} x {quantity} = ${product.price * quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


p1 = Product("Surface Laptop", 5000.00, 25)
p2 = Product("MacBook Air", 1000.00, 18)
p3 = Product("RTX 4050", 2000.00, 5)
p4 = Product("Asus Motherboard 14T", 1500.00, 12)
p1.display_info()
p2.display_info()
p3.display_info()
p4.display_info()

t = ShoppingCart()
t.add_item(p1, 5)
t.add_item(p2, 2)
t.add_item(p3, 1)
t.add_item(p4, 3)
t.calculate_total()

t.checkout()
