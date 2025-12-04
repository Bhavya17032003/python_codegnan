from login_module import accounts_table

def ministatement(username):
    print("\nMini Statement:")
    for txn in accounts_table[username]["statement"][-5:]:
        print("•", txn)
