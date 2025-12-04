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
    # checking the account number is exist in accounts table or not
    if username in accounts_table:
        # checking the password is correct or not
        if password == accounts_table[username]:
            print("Login successful")
            return True
        else:
            print("check with credentials")
    else:
        print("User Not Found")
        return False
    
# withdraw function definition
def withdraw(account:int, withdraw_amount:int):
    print("withdraw page")
# deposite function definition
def deposit(account:int, deposit_amount:int):
    print("deposit page")
# transfer function definition
def transfer(sender:int, receiver:int, transfer_amount:int):
    print("transfer page")
# ministatement function definition
def ministatement(account:int):
    print("minisatement page")
#logout function definition
def logout():
    print("Logout successfully")

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
                  "5. logout \n")
        print(*operations)
        choice = int(input("select your operation : "))
        if choice == 1:
            withdraw(account = username, withdraw_amount = 100)
        elif choice == 2:
            deposit(account = username, deposi_amount = 100)
        elif choice == 3:
            transfer(sender = username, receiver = 1235, transfer_amount = 100)
        elif choice == 4:
            ministatement(account = username)
        elif choice == 5:
            logout()
        else:
            print("select your operation in between 1 - 5")