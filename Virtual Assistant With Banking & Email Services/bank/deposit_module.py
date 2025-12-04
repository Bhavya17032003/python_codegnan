# deposit_module.py
from .bank_data import users_table, transactions
from email_modules.single_email_sender import singleEmailSender

def deposit(username, amount):
    if amount <= 0:
        print("Enter a valid amount.")
        return
    
    users_table[username][0] += amount
    transactions[username].append(f"Deposit: +{amount}")
    print(f"Deposit successful. Current balance: {users_table[username][0]}")

    # Send email notification
    user_email = users_table[username][2]
    subject = "Bank Transaction Alert"
    body = f"Dear {users_table[username][1]},\nYou have deposited {amount}. Current balance: {users_table[username][0]}"
    singleEmailSender(to_email=user_email, subject=subject, body=body)
