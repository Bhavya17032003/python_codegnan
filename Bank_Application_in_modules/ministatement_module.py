# ministatement_module.py
from bank_data import transactions

def ministatement(account: int):
    print("\n--- Mini Statement ---")
    if account in transactions:
        if transactions[account]:
            print("Your recent transactions:")
            for t in transactions[account]:
                print("-", t)
        else:
            print("No transactions yet.")
    else:
        print(" Account not found.")
