# Importing classes and funcions
from utils import errorMessage

# Transaction class that has all the functions for each Transaction
class Transactions:

    # Withdrawl function
    def withdrawal(self, loginType, name=None):
        # Getting account name if user is admin
        if loginType == 'admin':
            name = input("Please enter the account name you want to withdraw from:\n")
        
        # Getting account number and withdrawal amount
        accountNumber = input("Please enter the account number you want to withdraw from:\n")
        amount = input("Please enter the amount you want to withdraw:\n")

        # Displaying the amount withdrawn
        print("You withdrew $" + amount + " from " + name + "'s account " + accountNumber + "\n")

        return
    
    # Transfer function
    def transfer(self, loginType, name=None):
        # Getting account name if user is admin
        if loginType == 'admin':
            name = input("Please enter the account holder's name:\n")

        # Getting account numbers and transfer amount
        accountNumberFrom = input("Please enter the account number you want to transfer from:\n")
        accountNumberTo = input("Please enter the account number you want to transfer to:\n")
        amount = input("Please enter the amount you want to transfer:\n")

        # Displaying the amount transferred and from/to which accounts
        print("You are transferring $" + amount + " from " + name + "'s account " + accountNumberFrom + " to account " + accountNumberTo + "\n")

        return
    
    # Paybill function
    def paybill(self, loginType, name=None):
        # Checking if user is admin
        if loginType == 'admin':
            # Getting account name, number, amount and biller name
            name = input("Please enter the account holder's name:\n")
            accountNumber = input("Please enter the account number you want to pay from:\n")
            amount = input("Please enter the amount you want to pay:\n")
            billerName = input(
                "Please enter the biller name:\n"
                "Enter the two letter code for the biller you want to pay:\n"
                "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n"
            )

            # Displaying paybill information
            print("You are paying $" + amount + " from " + name + "'s account from account " + accountNumber + " to biller " +
                billerName + "\n")
        # Paybill function for standard users
        else:
            # Getting account number, amount and biller name
            accountNumber = input("Please enter the account number you want to pay from:\n")
            # Limiting amount to $2000.00 for standard users
            amount = input("Please enter the amount you want to pay:(max = $2000.00)\n")
            billerName = input(
                "Please enter the biller name:\n"
                "Enter the two letter code for the biller you want to pay:\n"
                "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n"
            )

            # Displaying paybill information
            print("You are paying $" + amount + " from " + name + "'s account from account " + accountNumber + " to biller " +
                billerName + "\n")

        return
    
    # Deposit function
    def deposit(self, loginType, name=None):
        # Checking if user is admin
        if loginType == 'admin':
            # Getting account name, number and amount
            name = input("Please enter the account name you want to deposit to:\n")
            accountNumberTo = input("Please enter the account number you want to deposit to:\n")
            amount = input("Please enter the amount you want to deposit:\n")
        # Deposit function for standard users
        else:
            # Getting account number and amount
            accountNumberTo = input("Please enter the account number you want to deposit to:\n")
            amount = input("Please enter the amount you want to deposit:\n")

        # Displaying deposit information
        print("You are depositing $" + amount + " to " + name +"'s account " + accountNumberTo + "\n")

        return
    
    # Create account function (admin only)
    def createAccount(self, loginType):
        # Checking if user is admin
        if loginType != 'admin':
            errorMessage("You do not have permission to create an account.\n")
            return
        
        # Getting account holder name, account number and initial balance
        accountHolderName = input("Please enter the account holder's name:\nMax name length is 20 characters\n")
        accountNumber = input("Please enter the account number you want to create:\n")
        initialBalance = input("Please enter the initial balance of the account:\nMax initial balance is $99,999.99\n")

        # Displaying account creation information
        print("You are creating an account for " +
              accountHolderName +
              " with account number " +
              accountNumber +
              " and initial balance $" +
              initialBalance + "\n")

        return
    
    # Delete account function (admin only)
    def deleteAccount(self, loginType):
        # Checking if user is admin
        if loginType != 'admin':
            errorMessage("You do not have permission to delete an account.\n")
            return
        
        # Getting account holder name and account number
        accountHolderName = input("Please enter the account holder's name:\n")
        accountNumber = input("Please enter the account number you want to delete:\n")

        # Displaying deleted account information
        print("You have deleted " +
              accountHolderName +
              "'s account with account number " +
              accountNumber + "\n")
        
        return
    
    # Disable account function (admin only)
    def disableAccount(self, loginType):
        # Checking if user is admin
        if loginType != 'admin':
            errorMessage("You do not have permission to disable an account.\n")
            return
        
        # Getting account holder name and account number
        accountHolderName = input("Please enter the account holder's name:\n")
        accountNumber = input("Please enter the account number you want to disable:\n")

        # Displaying disabled account information
        print("You have disabled " +
              accountHolderName +
              "'s account with account number " +
              accountNumber + "\n")
        
        return
    
    # Change account plan function (admin only)
    def changeplan(self, loginType):
        # Checking if user is admin
        if loginType != 'admin':
            errorMessage("You do not have permission to change an account plan.\n")
            return
        
        # Getting account holder name and account number
        accountHolderName = input("Please enter the account holder's name:\n")
        accountNumber = input("Please enter the account number you want to disable:\n")

        # Displaying changed plan information
        print("You haved changed " +
              accountHolderName +
              "'s account (" +
              accountNumber +
              ") to a non-student plan\n")
        
        return