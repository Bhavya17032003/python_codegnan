# balance_module.py
from .bank_data import users_table

def balance_enquiry(username):
    print(f"Your current balance is: {users_table[username][0]}")
