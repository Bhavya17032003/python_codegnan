from login_module import accounts_table
from email_sender_module import send_email

def withdraw(username, amount):
    if accounts_table[username]["balance"] >= amount:
        accounts_table[username]["balance"] -= amount
        accounts_table[username]["statement"].append(f"Withdraw: -₹{amount}")
        print(f"Withdrawal successful. New balance: ₹{accounts_table[username]['balance']}")
        
        subject = "Withdrawal Alert - Codegnan Bank"
        body = f"Dear {accounts_table[username]['name']},\n\nYou have withdrawn ₹{amount} from your account.\nYour current balance: ₹{accounts_table[username]['balance']}.\n\n- Codegnan Bank"
        send_email(accounts_table[username]["email"], subject, body)
    else:
        print("Insufficient funds.")
