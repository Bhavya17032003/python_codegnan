from login_module import accounts_table
from email_sender_module import send_email

def deposit(username, amount):
    accounts_table[username]["balance"] += amount
    accounts_table[username]["statement"].append(f"Deposit: +₹{amount}")
    print(f"Deposit successful. New balance: ₹{accounts_table[username]['balance']}")

    subject = "Deposit Alert - Codegnan Bank"
    body = f"Dear {accounts_table[username]['name']},\n\n₹{amount} has been deposited to your account.\nYour current balance: ₹{accounts_table[username]['balance']}.\n\n- Codegnan Bank"
    send_email(accounts_table[username]["email"], subject, body)
