# transfer_module.py
from bank_data import users_table, transactions
from datetime import datetime

def transfer(sender: int, receiver: int, transfer_amount: int):
    print("\n--- Transfer Page ---")
    if sender in users_table and receiver in users_table:
        if transfer_amount > 0 and transfer_amount <= users_table[sender][0]:
            users_table[sender][0] -= transfer_amount
            users_table[receiver][0] += transfer_amount
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transactions[sender].append(f"[{time}]Transferred ₹{transfer_amount} to {receiver}")
            transactions[receiver].append(f"[{time}]Received ₹{transfer_amount} from {sender}")
            print(f"₹{transfer_amount} transferred successfully. Sender balance: ₹{users_table[sender][0]}")
        else:
            print(" Insufficient balance or invalid amount.")
    else:
        print("Sender or receiver not found.")
