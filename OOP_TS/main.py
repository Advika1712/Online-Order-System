from OOP_TS.user_auth import login
from OOP_TS.order_services import show_products, add_to_cart, view_cart, place_order, make_payment, track_order, orders
from OOP_TS.data_manager import save_orders, load_orders, generate_report

if login():
    while True:
        print("""
--- Online Order Processing & Tracking System ---
1. Show Products
2. Add to Cart
3. View Cart
4. Place Order
5. Make Payment
6. Track Order
7. Save Orders
8. Load Orders
9. Generate Report
0. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            place_order()
        elif choice == "5":
            make_payment()
        elif choice == "6":
            track_order()
        elif choice == "7":
            save_orders(orders)
        elif choice == "8":
            load_orders()
        elif choice == "9":
            generate_report(orders)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

      
