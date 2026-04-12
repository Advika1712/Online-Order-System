import random

class Customer:
    def __init__(self, name, phone, address):
        self.customer_id = random.randint(1000, 9999)
        self.name = name
        self.phone = phone
        self.address = address


class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer, cart):
        self.order_id = random.randint(10000, 99999)
        self.customer = customer
        self.cart = cart  # list of (product, quantity)
        self.total_amount = self.calculate_total()
        self.status = "Pending"
      
    def calculate_total(self):
        total = 0
        for product, qty in self.cart:
            total += product.price * qty
        return total


class Payment:
    def __init__(self, order):
        self.order = order
        self.status = "Pending"

    def process_payment(self):
        self.status = "Successful"
        self.order.status = "Confirmed"


class Tracking:
    def __init__(self, order):
        self.order = order
        self.delivery_status = "Shipped"

    def update_status(self):
        self.delivery_status = "Delivered"
        self.order.status = "Delivered"
      
