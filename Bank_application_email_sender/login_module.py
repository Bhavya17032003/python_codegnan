accounts_table = {
    1234: {"password": 456, "name": "Bhavya", "email": "bhavyasreekanchukommala@gmail.com", "balance": 5000, "statement": []},
    5678: {"password": 999, "name": "Akky", "email": "bhavyakanchukommala@gmail.com", "balance": 3000, "statement": []}
}

def login(username, password):
    if username in accounts_table and accounts_table[username]["password"] == password:
        print(f"Welcome {accounts_table[username]['name']}!")
        return True
    else:
        print("Invalid account number or password.")
        return False
