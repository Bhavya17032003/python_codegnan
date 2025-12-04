# transfer_module.py
from .bank_data import users_table, transactions
from email_modules.single_email_sender import singleEmailSender

def transfer(sender_id, receiver_id, amount):
    if amount <= 0:
        print("Enter a valid amount.")
        return
    
    if sender_id not in users_table or receiver_id not in users_table:
        print("Invalid account number(s).")
        return
    
    if users_table[sender_id][0] >= amount:
        # Deduct from sender
        users_table[sender_id][0] -= amount
        transactions[sender_id].append(f"Transfer to {receiver_id}: -{amount}")

        # Add to receiver
        users_table[receiver_id][0] += amount
        transactions[receiver_id].append(f"Transfer from {sender_id}: +{amount}")

        print(f"Transfer successful. Your remaining balance: {users_table[sender_id][0]}")

        # Send email notifications
        sender_email = users_table[sender_id][2]
        receiver_email = users_table[receiver_id][2]

        sender_subject = "Bank Transaction Alert"
        sender_body = f"Dear {users_table[sender_id][1]},\nYou have transferred {amount} to account {receiver_id}. Remaining balance: {users_table[sender_id][0]}"
        singleEmailSender(to_email=sender_email, subject=sender_subject, body=sender_body)

        receiver_subject = "Bank Transaction Alert"
        receiver_body = f"Dear {users_table[receiver_id][1]},\nYou have received {amount} from account {sender_id}. Current balance: {users_table[receiver_id][0]}"
        singleEmailSender(to_email=receiver_email, subject=receiver_subject, body=receiver_body)
    else:
        print("Insufficient balance.")

