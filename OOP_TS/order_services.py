from OOP_TS.order_models import Customer, Product, Order, Payment, Tracking

import numpy as np

products = {
    "1": Product("1", "Laptop", 50000),
    "2": Product("2", "Phone", 20000),
    "3": Product("3", "Shoes", 3000)
}

orders = {}
cart = []


def show_products():
    print("\nAvailable Products:")
    for p in products.values():
        print(f"{p.pid} - {p.name} - ₹{p.price}")


def view_cart():
    if not cart:
        print("\nCart is empty!")
        return

    print("\n--- Your Cart ---")

    prices = []
    for product, qty in cart:
        amount = product.price * qty
        prices.append(amount)
        print(f"{product.name} x {qty} = ₹{amount}")

    total = np.sum(prices)
    print(f"Total (not ordered yet): ₹{total}")


def add_to_cart():
    show_products()
    pid = input("Enter Product ID: ")

    if pid not in products:
        print("Invalid product!")
        return

    quantity = int(input("Enter Quantity: "))
    cart.append((products[pid], quantity))

    print("Item added to cart!")


def place_order():
    if not cart:
        print("Cart is empty! Add items first.")
        return

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")

    customer = Customer(name, phone, address)

    order = Order(customer, cart.copy())
    orders[order.order_id] = order

    print("\nOrder placed successfully!")
    print(f"Order ID: {order.order_id}")

    print("\nItems in your order:")
    for product, qty in cart:
        print(f"{product.name} x {qty} = ₹{product.price * qty}")

    print(f"\nTotal Amount: ₹{order.total_amount}")

    cart.clear()


def make_payment():
    oid = int(input("Enter Order ID: "))
    if oid in orders:
        payment = Payment(orders[oid])
        payment.process_payment()
        print("Payment Successful!")
    else:
        print("Order not found")


def track_order():
    oid = int(input("Enter Order ID: "))
    if oid in orders:
        order = orders[oid]

        tracking = Tracking(order)
        tracking.update_status()

        print("\n--- Tracking Details ---")
        print(f"Order Status: {order.status}")
        print(f"Delivery Status: {tracking.delivery_status}")
    else:
        print("Order not found")

  
