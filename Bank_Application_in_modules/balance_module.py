# balance_module.py
from bank_data import users_table

def balance_enquiry(account: int):
    print("\n--- Balance Enquiry ---")
    if account in users_table:
        print(f"Current balance: ₹{users_table[account][0]}")
    else:
        print("Account not found.")
