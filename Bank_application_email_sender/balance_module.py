from login_module import accounts_table

def balance_enquiry(username):
    print(f"Current Balance: ₹{accounts_table[username]['balance']}")
