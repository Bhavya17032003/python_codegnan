#creating table 
#accounts_table = {account: password}
#users_table = {account:[account,Name,email]}
accounts_table = {1234:456, 1235:457}
users_table = {1234:[1000,'Bhavya','bhavyasreekanchukommala@gmail.com'], 
               1235:[500, 'Bannu','bhavyakanchukommala@gmail.com']}

 #functions
 # #login function definition
def login(username:int, password:int):
    print("Login page")
    # checking the account number in account table or not
    if username in accounts_table:
        # checking the password is correct or not
        if password == accounts_table[username]:
            print("Login successful ")
            return True
        else:
            print("check with credentials")
            return False
    else:
        print("User Not Found")
       
        
    
# withdraw function definition
def withdraw(account:int, withdraw_amount:int):
    print("withdraw page")
    # checking account in users or not
    if account in users_table:
        amount = users_table[account][0]
        #checking amount is sufficient or not
        if amount >= withdraw_amount:
            users_table[account][0]-=withdraw_amount
            print(f"{withdraw_amount} withdraw successful and current balance is:{users_table[account][0]}")
        else:
            print("Insufficient amount in your account")
    else:
        print("user not found")


# deposit function definition
def deposit(account:int, deposit_amount:int):
    print("deposit page")
    if account in users_table:
        if deposit_amount > 0:
            users_table[account][0]+=deposit_amount
            print(f"{deposit_amount} deposit successful and current balance is:{users_table[account][0]}")
        else:
            print("check with your deposit amount")
    else:
        print("user not found")


# transfer function definition
def transfer(sender:int, receiver:int, transfer_amount:int):
    print("transfer page")
    # checking that sender and receiver present in users table or not
    if sender in users_table and receiver in users_table:
        if transfer_amount <= users_table[sender][0]:
            users_table[sender][0]-=transfer_amount
            users_table[receiver][0]+=transfer_amount
            print(f"{transfer_amount} transfer successful and current balance is:{users_table[sender][0]}")
        else:
            print("Insufficient balance in your account")
    else:
        print("User not found")


# ministatement function definition
def ministatement(account:int):
    print("minisatement page development under processing")

#balance enquiry function definition
def balance_enquiry(account:int):
    if account in users_table:
        print(f"current balance is:{users_table[account][0]}")
    else:
        print("user not found")


#logout function definition
def logout():
    print("Logout successfully")
    exit()

# main
if __name__ == "__main__":
    print("welocme to the codegnan Bank Application")
    username = int(input("Enter your account number: "))
    password = int(input("Enter your password: "))
    login_val = login(username = username, password = password)
    while True:
        operations = ("1. Withdraw \n"
                  "2. Deposit \n"
                  "3. Transfer\n"
                  "4. mini statement\n"
                  "5. balance enquiry \n"
                  "6. logout \n")
        print(*operations)
        choice = int(input("select your operation : "))
        if choice == 1:
            withdraw(account = username, withdraw_amount = int(input("Enter withdraw amount: ")))
        elif choice == 2:
            deposit(account = username, deposit_amount = int(input("Enter deposit amount: ")))
        elif choice == 3:
            transfer(sender = username, receiver = int(input("Enter account amount: ")), transfer_amount = int(input("Enter amount: ")))                                                                                             
        elif choice == 4:
            ministatement(account = username)
        elif choice == 5:
            balance_enquiry(account = username)
        elif choice == 6:
            logout()
        else:
            print("select your operation in between 1 - 5 ")