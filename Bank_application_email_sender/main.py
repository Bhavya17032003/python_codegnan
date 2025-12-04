from login_module import login, accounts_table
from withdraw_module import withdraw
from deposit_module import deposit
from transfer_module import transfer
from ministatement_module import ministatement
from balance_module import balance_enquiry
from logout_module import logout

print("Welcome to Codegnan Bank Application")

username = int(input("Enter your account number: "))
password = int(input("Enter your password: "))

if login(username, password):
    while True:
        print("""
----------------------------------
1. Withdraw
2. Deposit
3. Transfer
4. Mini Statement
5. Balance Enquiry
6. Logout
----------------------------------
""")
        choice = int(input("Select your operation (1-6): "))

        if choice == 1:
            withdraw(username, int(input("Enter withdraw amount: ")))

        elif choice == 2:
            deposit(username, int(input("Enter deposit amount: ")))

        elif choice == 3:
            receiver = int(input("Enter receiver account number: "))
            amount = int(input("Enter transfer amount: "))
            transfer(username, receiver, amount)

        elif choice == 4:
            ministatement(username)

        elif choice == 5:
            balance_enquiry(username)

        elif choice == 6:
            logout()
            break

        else:
            print("Please choose a valid option (1-6).")
else:
    print("Login failed. Exiting the application.")
