USERS = {
    "admin": "1234"
}

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if USERS.get(username) == password:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Login!\n")
        return False
