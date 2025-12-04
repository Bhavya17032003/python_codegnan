from .bank_data import users_table, transactions
from email_modules.single_email_sender import singleEmailSender

def withdraw(username, amount):
    if amount <= 0:
        print("Enter a valid amount.")
        return
    if users_table[username][0] >= amount:
        users_table[username][0] -= amount
        transactions[username].append(f"Withdraw: -{amount}")
        print(f"Withdrawal successful. Remaining balance: {users_table[username][0]}")

        # Send email notification
        user_email = users_table[username][2]
        subject = "Bank Transaction Alert"
        body = f"Dear {users_table[username][1]},\nYou have withdrawn {amount}. Remaining balance: {users_table[username][0]}"
        singleEmailSender(to_email=user_email, subject=subject, body=body)
    else:
        print("Insufficient balance.")
