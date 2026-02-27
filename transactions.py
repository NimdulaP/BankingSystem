import os

class Transactions:
    def __init__(self):
        self.transaction_file = self.create_new_session_file("daily_transactions_")

    # FORMATTER FUNCTION
    def write_transaction(self, code, name="", acc_num="0", amount="0", misc="00"):
        # Code: 2 digits, zero-padded
        code_field = f"{int(code):02d}"

        if code == 0:
            # End-of-session
            name_field = "END_OF_SESSION".ljust(20, "_")
            acc_field = "00000"
            amount_field = "00000.00"
            misc_field = "00"
        else:
            # Name: 20 chars, space-filled replacing existing spaces with _
            name_field = name.replace(" ", "_").ljust(20, "_")
            
            # Account: 5 digits, zero-padded
            acc_field = f"{int(acc_num):05d}"
            
            # Amount: 8 chars ensures 2 decimal places
            amount_field = f"{float(amount):08.2f}"
            
            # Misc: 2 chars
            misc_field = misc.ljust(2)

        # Assemble with the required spaces between each field
        line = f"{code_field}_{name_field}_{acc_field}_{amount_field}_{misc_field}"
        
        self.append_to_session_file(line)

    # File handling functions
    def create_new_session_file(self, base_filename):
        os.makedirs("daily_transactions", exist_ok=True)
        i = 1
        filename = os.path.join("daily_transactions", f"{base_filename}{i}.txt")

        while os.path.exists(filename):
            i += 1
            filename = os.path.join("daily_transactions", f"{base_filename}{i}.txt") 

        # Create the file once per run
        with open(filename, "w", encoding="utf-8") as f:
            # empty file to start session
            f.write("")  

        return filename

    def append_to_session_file(self, transaction):
        with open(self.transaction_file, "a", encoding="utf-8") as f:
            f.write(transaction + "\n")

    # TRANSACTIONS

    # Withdrawl function
    def withdrawal(self, loginType, name=None):
        # Getting account name if user is admin
        if loginType == "admin":
            name = input("Please enter the account name you want to withdraw from:\n")
        # Getting account number and withdrawal amount
        accountNumber = input("Please enter the account number you want to withdraw from:\n")
        amount = input("Please enter the amount you want to withdraw:\n")
        # Displaying the amount withdrawn
        print(f"You withdrew ${amount} from {name}'s account {accountNumber}\n")
        # Writing transaction to file
        self.write_transaction(1, name, accountNumber, amount)

    # Transfer function
    def transfer(self, loginType, name=None):
        # Getting account name if user is admin
        if loginType == "admin":
            name = input("Please enter the account holder's name:\n")

        # Getting account numbers and transfer amount
        accountNumberFrom = input("Please enter the account number you want to transfer from:\n")
        accountNumberTo = input("Please enter the account number you want to transfer to:\n")
        amount = input("Please enter the amount you want to transfer:\n")

        # Displaying the amount transferred and from/to which accounts
        print(f"You are transferring ${amount} from {name}'s account {accountNumberFrom} to account {accountNumberTo}\n")

        # Writing transaction to file
        self.write_transaction(2, name, accountNumberFrom, amount)

    # Paybill function
    def paybill(self, loginType, name=None):
        # Checking if user is admin
        if loginType == "admin":
            name = input("Please enter the account holder's name:\n")

        # Getting account number, amount and biller name
        accountNumber = input("Please enter the account number you want to pay from:\n")
        amount = input("Please enter the amount you want to pay:\n")
        biller = input("Enter biller code (EC, CQ, FI):\n")

        # Displaying paybill information
        print(f"You are paying ${amount} from {name}'s account {accountNumber} to biller {biller}\n")
        # Writing transaction to file
        self.write_transaction(3, name, accountNumber, amount, biller)

    # Deposit function
    def deposit(self, loginType, name=None):
        # Getting account name if user is admin
        if loginType == "admin":
            name = input("Please enter the account name you want to deposit to:\n")
        # Getting account number and amount
        accountNumber = input("Please enter the account number you want to deposit to:\n")
        amount = input("Please enter the amount you want to deposit:\n")
        # Displaying deposit information
        print(f"You are depositing ${amount} to {name}'s account {accountNumber}\n")
        # Writing transaction to file
        self.write_transaction(4, name, accountNumber, amount)

    # Admin-only functions
    def createAccount(self, loginType):
        # Checking if user is admin
        if loginType != "admin":
            print("You do not have permission to create an account.\n")
            return
        # Getting account holder name, account number and initial balance
        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number you want to create:\n")
        balance = input("Please enter the initial balance:\n")
        # Displaying account creation information
        print(f"You are creating an account for {name} with account number {acc} and balance ${balance}\n")
        # Writing transaction to file
        self.write_transaction(5, name, acc, balance)


    def deleteAccount(self, loginType):
        # Checking if user is admin 
        if loginType != "admin":
            print("You do not have permission.\n")
            return
        # Getting account holder name and account number    
        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number you want to delete:\n")
        # Displaying deleted account information
        print(f"You have deleted {name}'s account {acc}\n")
        # Writing transaction to file
        self.write_transaction(6, name, acc, "0")


    def disableAccount(self, loginType):
        # Checking if user is admin 
        if loginType != "admin":
            print("You do not have permission.\n")
            return
        # Getting account holder name and account number
        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number you want to disable:\n")
        # Displaying disabled account information
        print(f"You have disabled {name}'s account {acc}\n")
        # Writing transaction to file   
        self.write_transaction(7, name, acc, "0")


    def changeplan(self, loginType):
        # Checking if user is admin
        if loginType != "admin":
            print("You do not have permission.\n")
            return
        # Getting account holder name and account number
        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number:\n")
        # Displaying changed plan information
        print(f"You changed {name}'s account {acc} plan\n")
        # Writing transaction to file
        self.write_transaction(8, name, acc, "0")