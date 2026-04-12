import json
import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "orders_data.json"

def save_orders(orders):
    data = {}

    for oid, order in orders.items():
        items = []
        for product, qty in order.cart:
            items.append({
                "product": product.name,
                "quantity": qty,
                "price": product.price
            })

        data[str(oid)] = {
            "customer": order.customer.name,
            "items": items,
            "total": order.total_amount,
            "status": order.status
        }

    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

    print("Orders saved successfully!")


def load_orders():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            print("Orders loaded successfully!")
            return data
    except FileNotFoundError:
        print("No previous data found.")
        return {}


def generate_report(orders):
    if not orders:
        print("No orders to analyze.")
        return

    data = []

    for oid, order in orders.items():
        for product, qty in order.cart:
            data.append({
                "OrderID": oid,
                "Product": product.name,
                "Quantity": qty,
                "Amount": product.price * qty
            })

    df = pd.DataFrame(data)

    print("\n--- Order Report ---")
    print(df)

    df.groupby("Product")["Amount"].sum().plot(kind='bar')
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.show()

