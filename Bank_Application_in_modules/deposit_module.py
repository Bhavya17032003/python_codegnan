# deposit_module.py
from bank_data import users_table, transactions
from datetime import datetime

def deposit(account: int, deposit_amount: int):
    print("\n--- Deposit Page ---")
    if account in users_table:
        if deposit_amount > 0:
            users_table[account][0] += deposit_amount
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transactions[account].append(f"[{time}]Deposited ₹{deposit_amount}")
            print(f"₹{deposit_amount} deposited successfully. Current balance: ₹{users_table[account][0]}")
        else:
            print("Invalid deposit amount.")
    else:
        print("Account not found.")
