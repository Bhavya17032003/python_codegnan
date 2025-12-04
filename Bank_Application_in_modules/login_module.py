# login_module.py
from bank_data import accounts_table

def login(username: int, password: int):
    print("\n--- Login Page ---")
    if username in accounts_table:
        if password == accounts_table[username]:
            print("Login successful\n")
            return True
        else:
            print(" Incorrect password.\n")
            return False
    else:
        print("User not found.\n")
        return False
