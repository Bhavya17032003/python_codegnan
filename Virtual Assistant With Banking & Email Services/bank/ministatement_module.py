# ministatement_module.py
from .bank_data import transactions, users_table

def ministatement(username):
    print(f"\n--- Mini Statement for {users_table[username][1]} ---")
    if transactions[username]:
        for txn in transactions[username][-5:]:  # last 5 transactions
            print(txn)
    else:
        print("No transactions yet.")
    print(f"Current balance: {users_table[username][0]}")
