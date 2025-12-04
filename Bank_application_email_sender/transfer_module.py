from login_module import accounts_table
from email_sender_module import send_email

def transfer(sender, receiver, amount):
    if receiver not in accounts_table:
        print("Receiver account not found.")
        return
    
    if accounts_table[sender]["balance"] >= amount:
        accounts_table[sender]["balance"] -= amount
        accounts_table[receiver]["balance"] += amount
        accounts_table[sender]["statement"].append(f"Transfer: -₹{amount} to {receiver}")
        accounts_table[receiver]["statement"].append(f"Transfer: +₹{amount} from {sender}")
        print(f"Transfer of ₹{amount} to account {receiver} successful.")

        # Email alerts
        send_email(accounts_table[sender]["email"],
                   "Transfer Alert - Codegnan Bank",
                   f"Dear {accounts_table[sender]['name']},\n\nYou transferred ₹{amount} to account {receiver}.\nYour balance: ₹{accounts_table[sender]['balance']}.\n\n- Codegnan Bank")

        send_email(accounts_table[receiver]["email"],
                   "Credit Alert - Codegnan Bank",
                   f"Dear {accounts_table[receiver]['name']},\n\nYou received ₹{amount} from account {sender}.\nYour balance: ₹{accounts_table[receiver]['balance']}.\n\n- Codegnan Bank")
    else:
        print("Insufficient funds.")
