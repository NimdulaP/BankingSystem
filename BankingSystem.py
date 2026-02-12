# Source - https://stackoverflow.com/a/287944
# Posted by joeld, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-12, License - CC BY-SA 4.0
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def readFile():
    with open('accounts.txt') as file:
        lines = [line.rstrip() for line in file]
    

def showOptions(loginType):
    while True:
        print("Enter the number of the option you want to proceed with")
        if loginType == 'a':
            print("1. Withdrawl\n2. Transfer\n3. Paybill\n4. Deposit\n5. Create Account\n6. Delete Account\n7. Disable Account\n8. Changeplan\n9. Logout")
            choice = input()
            try:
                choiceInt = int(choice)
                if choiceInt >= 1 and choiceInt <= 9:
                    return choice
                else:
                    errorMessage("Please enter a valid choice number")
            except ValueError:
                errorMessage("Please enter a number")
        else:
            print("1. Withdrawl\n2. Transfer\n3. Paybill\n4. Deposit\n5. Logout")
            choice = input()
            try:
                choiceInt = int(choice)
                if choiceInt >= 1 and choiceInt <= 5:
                    return choice
                else:
                    errorMessage("Please enter a valid choice number")
            except ValueError:
                errorMessage("Please enter a number")

def errorMessage(message):
    print(bcolors.FAIL + message + bcolors.ENDC)

def withdrawl():
    if loginType == 'a':
        print("Please enter the account number you want to withdraw from:\n")
        accountNumber = input()
        print("Please enter the amount you want to withdraw:\n")
        amount = input()
    else:
        return
        
def transfer():
    print("transfer")
    if loginType == 'a':
        print("Please enter the account holder's name:\n")
        accountHolderName = input()
    print("Please enter the account number you want to transfer from:\n")
    accountNumberFrom = input()
    print("Please enter the account number you want to transfer to:\n")
    accountNumberTo = input()
    print("Please enter the amount you want to transfer:\n")
    amount = input()
    # dislpay transfer details
    print("You are transferring $" + amount + " from " + accountHolderName+ "'s account " + accountNumberFrom + " to account " + accountNumberTo + "\n")
   
    return

def paybill():
    if loginType == 'a':
        print
        print("Please enter the account number you want to pay from:\n")
        accountNumberFrom = input()
        print("Please enter the amount you want to pay:\n")
        amount = input()
        print("Please enter the biller name:\n" +
            "Enter the two letter code for the biller you want to pay: \n" 
            "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n")
        billerName = input()

        print("You are paying $" + amount + " from account " + accountNumberFrom + " to biller " + billerName + "\n")
    else:
        print("Please enter the account number you want to pay from:\n")
        accountNumberFrom = input()
        print("Please enter the amount you want to pay:(max = $2000.00)\n")
        amount = input()
        print("Please enter the biller name:\n" +
            "Enter the two letter code for the biller you want to pay: \n" 
            "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n")
        billerName = input()

        print("You are paying $" + amount + " from account " + accountNumberFrom + " to biller " + billerName + "\n")
    return

def deposit():
    if loginType == 'a':
        print("Please enter the account name you want to deposit to:\n")
        accountNameTo = input()
        print("Please enter the account number you want to deposit to:\n")
        accountNumberTo = input()
        print("Please enter the amount you want to deposit:\n")
        amount = input()
    else:
        print("Please enter the account number you want to deposit to:\n")
        accountNumberTo = input()
        print("Please enter the amount you want to deposit:\n")
        amount = input()
    return

def createAccount():
    return

def deleteAccount():
    return

def disableAccount():
    return

def changeplan():
    return

def title(text):
    print(bcolors.BOLD + bcolors.OKBLUE + "\n" + text + bcolors.ENDC)


def findAccountName():
    print("Please enter account name:")
    name = input()
    # with open('accounts.txt') as file:
    #     lines = [line.rstrip() for line in file]
    #     for line in lines:
    #         if name in line:
    #             print("Found name " + name)
    #             return name
    
    # errorMessage("Account name not found")

def goToTranscation(number):
    if number == '1':
        title('WITHDRAWL')
        withdrawl()
    elif number == '2':
        title('TRANSFEER')
        transfer()
    elif number == '3':
        title('PAYBILL')
        paybill()
    elif number == '4':
        title('DEPOSIT')
        deposit()
    elif number == '5':
        title('CREATE ACCOUNT')
        createAccount()
    elif number == '6':
        title('DELETE ACCOUNT')
        deleteAccount()
    elif number == '7':
        title('DISABLE ACCOUNT')
        disableAccount()
    else:
        title('CHANGE PLAN')
        changeplan()

loggedIn = True

while loggedIn:
    readFile()
    print("Welcome to the banking system.")
    print("For Standard Users, type 'S'.")
    print("For Admin Users, type 'A'")
    print("Please enter your login type:")
    loginType = input().lower()

    if loginType == 'a':
        print("You selected: 'Admin'")
        while True:
            mainChoice = showOptions(loginType)
            if mainChoice == '9':
                title("LOGGED OUT")
                loggedIn = False
                break
            else:
                goToTranscation(mainChoice)

    elif loginType == 's':
        print("You selected: 'Standard'")
        name = findAccountName()
        while True:
            mainChoice = showOptions(loginType)
            if mainChoice == '5': 
                title("LOGGED OUT")
                loggedIn = False
                break
            else:
                goToTranscation(mainChoice)
    else:
        errorMessage("Please enter a valid login type")