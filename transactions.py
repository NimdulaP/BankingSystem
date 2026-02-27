# from utils import errorMessage
import os

class Transactions:

    def __init__(self):
        self.transaction_file = self.create_new_session_file("daily_transactions_")

    # ==============================
    # FORMATTER FUNCTION (40 chars)
    # ==============================

    def write_transaction(self, code, name="", acc_num="0", amount="0", misc="00"):
        # CC: 2 digits
        code_field = f"{int(code):02d}"

        if code == 0:
            # End-of-session
            name_field = "END_OF_SESSION".ljust(20, "_")
            acc_field = "00000"
            amount_field = "00000.00"
            misc_field = "00"
        else:
            # Name: 20 chars, space-filled (replacing existing spaces with _)
            # Spec says "John Doe" -> "John_Doe____________"
            name_field = name.replace(" ", "_").ljust(20, "_")
            
            # Account: 5 digits, zero-padded
            acc_field = f"{int(acc_num):05d}"
            
            # Amount: 8 chars (e.g., 00110.00)
            # The format string ensures 2 decimal places
            amount_field = f"{float(amount):08.2f}"
            
            # Misc: 2 chars, left-justified
            misc_field = misc.ljust(2)

        # Assemble with the required spaces between each field
        # CC + space + Name + space + Acc + space + Amount + space + Misc
        line = f"{code_field}_{name_field}_{acc_field}_{amount_field}{misc_field}"
        
        # Verify length: 2 + 1 + 20 + 1 + 5 + 1 + 8 + 1 + 2 = 41 characters total
        # (The spec says 40 chars, but the field breakdown including spaces totals 41)
        # Please double-check if your professor defines 40 as the line length 
        # excluding the spaces, or if the field widths were meant to be smaller.
        
        # print(f"Formatted transaction line: '{line}' (length: {len(line)})")
        # self.transaction_file.write(line + "\n")
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
            f.write("")  # empty file to start session

        return filename

    def append_to_session_file(self, transaction):
        with open(self.transaction_file, "a", encoding="utf-8") as f:
            f.write(transaction + "\n")


    # ==============================
    # TRANSACTIONS
    # ==============================

    def withdrawal(self, loginType, name=None):

        if loginType == "admin":
            name = input("Please enter the account name you want to withdraw from:\n")

        acc = input("Please enter the account number you want to withdraw from:\n")
        amount = input("Please enter the amount you want to withdraw:\n")

        print(f"You withdrew ${amount} from {name}'s account {acc}\n")

        self.write_transaction(1, name, acc, amount)


    def transfer(self, loginType, name=None):

        if loginType == "admin":
            name = input("Please enter the account holder's name:\n")

        acc_from = input("Please enter the account number you want to transfer from:\n")
        acc_to = input("Please enter the account number you want to transfer to:\n")
        amount = input("Please enter the amount you want to transfer:\n")

        print(f"You are transferring ${amount} from {name}'s account {acc_from} to account {acc_to}\n")

        self.write_transaction(2, name, acc_from, amount)


    def paybill(self, loginType, name=None):

        if loginType == "admin":
            name = input("Please enter the account holder's name:\n")

        acc = input("Please enter the account number you want to pay from:\n")
        amount = input("Please enter the amount you want to pay:\n")
        biller = input("Enter biller code (EC, CQ, FI):\n")

        print(f"You are paying ${amount} from {name}'s account {acc} to biller {biller}\n")

        self.write_transaction(3, name, acc, amount, biller)


    def deposit(self, loginType, name=None):

        if loginType == "admin":
            name = input("Please enter the account name you want to deposit to:\n")

        acc = input("Please enter the account number you want to deposit to:\n")
        amount = input("Please enter the amount you want to deposit:\n")

        print(f"You are depositing ${amount} to {name}'s account {acc}\n")

        self.write_transaction(4, name, acc, amount)


    def createAccount(self, loginType):

        if loginType != "admin":
            print("You do not have permission to create an account.\n")
            return

        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number you want to create:\n")
        balance = input("Please enter the initial balance:\n")

        print(f"You are creating an account for {name} with account number {acc} and balance ${balance}\n")

        self.write_transaction(5, name, acc, balance)


    def deleteAccount(self, loginType):

        if loginType != "admin":
            print("You do not have permission.\n")
            return

        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number you want to delete:\n")

        print(f"You have deleted {name}'s account {acc}\n")

        self.write_transaction(6, name, acc, "0")


    def disableAccount(self, loginType):

        if loginType != "admin":
            print("You do not have permission.\n")
            return

        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number you want to disable:\n")

        print(f"You have disabled {name}'s account {acc}\n")

        self.write_transaction(7, name, acc, "0")


    def changeplan(self, loginType):

        if loginType != "admin":
            print("You do not have permission.\n")
            return

        name = input("Please enter the account holder's name:\n")
        acc = input("Please enter the account number:\n")

        print(f"You changed {name}'s account {acc} plan\n")

        self.write_transaction(8, name, acc, "0")



# # Importing classes and funcions
# from utils import errorMessage

# # Transaction class that has all the functions for each Transaction
# class Transactions:

#     # Withdrawl function
#     def withdrawal(self, loginType, name=None):
#         # Getting account name if user is admin
#         if loginType == 'admin':
#             name = input("Please enter the account name you want to withdraw from:\n")
        
#         # Getting account number and withdrawal amount
#         accountNumber = input("Please enter the account number you want to withdraw from:\n")
#         amount = input("Please enter the amount you want to withdraw:\n")

#         # Displaying the amount withdrawn
#         print("You withdrew $" + amount + " from " + name + "'s account " + accountNumber + "\n")

#         return
    
#     # Transfer function
#     def transfer(self, loginType, name=None):
#         # Getting account name if user is admin
#         if loginType == 'admin':
#             name = input("Please enter the account holder's name:\n")

#         # Getting account numbers and transfer amount
#         accountNumberFrom = input("Please enter the account number you want to transfer from:\n")
#         accountNumberTo = input("Please enter the account number you want to transfer to:\n")
#         amount = input("Please enter the amount you want to transfer:\n")

#         # Displaying the amount transferred and from/to which accounts
#         print("You are transferring $" + amount + " from " + name + "'s account " + accountNumberFrom + " to account " + accountNumberTo + "\n")

#         return
    
#     # Paybill function
#     def paybill(self, loginType, name=None):
#         # Checking if user is admin
#         if loginType == 'admin':
#             # Getting account name, number, amount and biller name
#             name = input("Please enter the account holder's name:\n")
#             accountNumber = input("Please enter the account number you want to pay from:\n")
#             amount = input("Please enter the amount you want to pay:\n")
#             billerName = input(
#                 "Please enter the biller name:\n"
#                 "Enter the two letter code for the biller you want to pay:\n"
#                 "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n"
#             )

#             # Displaying paybill information
#             print("You are paying $" + amount + " from " + name + "'s account from account " + accountNumber + " to biller " +
#                 billerName + "\n")
#         # Paybill function for standard users
#         else:
#             # Getting account number, amount and biller name
#             accountNumber = input("Please enter the account number you want to pay from:\n")
#             # Limiting amount to $2000.00 for standard users
#             amount = input("Please enter the amount you want to pay:(max = $2000.00)\n")
#             billerName = input(
#                 "Please enter the biller name:\n"
#                 "Enter the two letter code for the biller you want to pay:\n"
#                 "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n"
#             )

#             # Displaying paybill information
#             print("You are paying $" + amount + " from " + name + "'s account from account " + accountNumber + " to biller " +
#                 billerName + "\n")

#         return
    
#     # Deposit function
#     def deposit(self, loginType, name=None):
#         # Checking if user is admin
#         if loginType == 'admin':
#             # Getting account name, number and amount
#             name = input("Please enter the account name you want to deposit to:\n")
#             accountNumberTo = input("Please enter the account number you want to deposit to:\n")
#             amount = input("Please enter the amount you want to deposit:\n")
#         # Deposit function for standard users
#         else:
#             # Getting account number and amount
#             accountNumberTo = input("Please enter the account number you want to deposit to:\n")
#             amount = input("Please enter the amount you want to deposit:\n")

#         # Displaying deposit information
#         print("You are depositing $" + amount + " to " + name +"'s account " + accountNumberTo + "\n")

#         return
    
#     # Create account function (admin only)
#     def createAccount(self, loginType):
#         # Checking if user is admin
#         if loginType != 'admin':
#             errorMessage("You do not have permission to create an account.\n")
#             return
        
#         # Getting account holder name, account number and initial balance
#         accountHolderName = input("Please enter the account holder's name:\nMax name length is 20 characters\n")
#         accountNumber = input("Please enter the account number you want to create:\n")
#         initialBalance = input("Please enter the initial balance of the account:\nMax initial balance is $99,999.99\n")

#         # Displaying account creation information
#         print("You are creating an account for " +
#               accountHolderName +
#               " with account number " +
#               accountNumber +
#               " and initial balance $" +
#               initialBalance + "\n")

#         return
    
#     # Delete account function (admin only)
#     def deleteAccount(self, loginType):
#         # Checking if user is admin
#         if loginType != 'admin':
#             errorMessage("You do not have permission to delete an account.\n")
#             return
        
#         # Getting account holder name and account number
#         accountHolderName = input("Please enter the account holder's name:\n")
#         accountNumber = input("Please enter the account number you want to delete:\n")

#         # Displaying deleted account information
#         print("You have deleted " +
#               accountHolderName +
#               "'s account with account number " +
#               accountNumber + "\n")
        
#         return
    
#     # Disable account function (admin only)
#     def disableAccount(self, loginType):
#         # Checking if user is admin
#         if loginType != 'admin':
#             errorMessage("You do not have permission to disable an account.\n")
#             return
        
#         # Getting account holder name and account number
#         accountHolderName = input("Please enter the account holder's name:\n")
#         accountNumber = input("Please enter the account number you want to disable:\n")

#         # Displaying disabled account information
#         print("You have disabled " +
#               accountHolderName +
#               "'s account with account number " +
#               accountNumber + "\n")
        
#         return
    
#     # Change account plan function (admin only)
#     def changeplan(self, loginType):
#         # Checking if user is admin
#         if loginType != 'admin':
#             errorMessage("You do not have permission to change an account plan.\n")
#             return
        
#         # Getting account holder name and account number
#         accountHolderName = input("Please enter the account holder's name:\n")
#         accountNumber = input("Please enter the account number you want to disable:\n")

#         # Displaying changed plan information
#         print("You haved changed " +
#               accountHolderName +
#               "'s account (" +
#               accountNumber +
#               ") to a non-student plan\n")
        
#         return