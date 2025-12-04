# withdraw_module.py
from bank_data import users_table, transactions
from datetime import datetime

def withdraw(account: int, withdraw_amount: int):
    print("\n--- Withdraw Page ---")
    if account in users_table:
        balance = users_table[account][0]
        if withdraw_amount > 0 and balance >= withdraw_amount:
            users_table[account][0] -= withdraw_amount
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transactions[account].append(f"[{time}]Withdrawn ₹{withdraw_amount}")
            print(f"₹{withdraw_amount} withdrawn successfully. Current balance: ₹{users_table[account][0]}")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("Account not found.")
