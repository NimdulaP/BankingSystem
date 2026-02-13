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
    

def errorMessage(message):
    print(bcolors.FAIL + message + bcolors.ENDC)

def title(text):
    print(bcolors.BOLD + bcolors.OKBLUE + "\n" + text + bcolors.ENDC)

def withdrawl(loginType):
    if loginType == 'admin':
        accountNumber = input("Please enter the account number you want to withdraw from:\n")
    amount = input("Please enter the amount you want to withdraw:\n")
    print("You withdrew $" + amount)
    return 
        
def transfer(loginType):
    # placeholder for account holder name, if admin is logged in, they can specify 
    # the account holder name, otherwise it will be set to "standard user"
    accountHolderName = "standard user"
    if loginType == 'admin':
        accountHolderName = input("Please enter the account holder's name:\n")
    accountNumberFrom = input("Please enter the account number you want to transfer from:\n")
    accountNumberTo = input("Please enter the account number you want to transfer to:\n")
    amount = input("Please enter the amount you want to transfer:\n")
    # dislpay transfer details
    print("You are transferring $" + amount + " from " + accountHolderName+ "'s account " + accountNumberFrom + " to account " + accountNumberTo + "\n")
   
    return 

def paybill(loginType):
    if loginType == 'admin':
        accountHolderName = input("Please enter the account holder's name:\n")
        accountNumberFrom = input("Please enter the account number you want to pay from:\n")
        amount = input("Please enter the amount you want to pay:\n")
        billerName = input(
            "Please enter the biller name:\n" +
            "Enter the two letter code for the biller you want to pay: \n" 
            "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n")

        print("You are paying $" + amount + "from " + accountHolderName + "'s acount " +" from account " + accountNumberFrom + " to biller " + billerName + "\n")
    else:
        accountNumberFrom = input("Please enter the account number you want to pay from:\n")
        amount = input("Please enter the amount you want to pay:(max = $2000.00)\n")
        billerName = input("Please enter the biller name:\n" +
            "Enter the two letter code for the biller you want to pay: \n" 
            "The Bright Light Electric Company (EC), Credit Card Company Q (CQ) or Fast Internet, Inc. (FI)\n")

        print("You are paying $" + amount + " from account " + accountNumberFrom + " to biller " + billerName + "\n")

    return 

def deposit(loginType):
    accountNameTo = "standard user"
    if loginType == 'admin':
        accountNameTo = input("Please enter the account name you want to deposit to:\n")
        accountNumberTo = input("Please enter the account number you want to deposit to:\n")
        amount = input("Please enter the amount you want to deposit:\n")
    else:
        accountNumberTo = input("Please enter the account number you want to deposit to:\n")
        amount = input("Please enter the amount you want to deposit:\n")
    print("You are depositing $" + amount + " to " + accountNameTo + "'s account " + accountNumberTo + "\n")

    return 

def createAccount(loginType):
    accountHolderName = input("Please enter the account holder's name:\n" + 
          "Max name length is 20 characters\n")
    accountNumber = input("Please enter the account number you want to create:\n")

    initialBalance = input("Please enter the initial balance of the account:\n" + 
          "Max initial balance is $99,999.99\n")

    print("You are creating an account for " + accountHolderName + " with account number " + accountNumber + " and initial balance $" + initialBalance + "\n")
    return

def deleteAccount(loginType):
    accountHolderName = input("Please enter the account holder's name:\n") 
    accountNumber = input("Please enter the account number you want to delete:\n")
    print("You have deleted " + accountHolderName + "'s account with account number " + accountNumber + "\n")
    return 

def disableAccount(loginType):
    accountHolderName = input("Please enter the account holder's name:\n") 
    accountNumber = input("Please enter the account number you want to disable:\n")
    print("You haved disabled " + accountHolderName + "'s account with account number " + accountNumber + "\n")
    return 

def changeplan(loginType):
    accountHolderName = input("Please enter the account holder's name:\n") 
    accountNumber = input("Please enter the account number you want to disable:\n")
    print("You haved changed " + accountHolderName + "'s account (" + accountNumber + ") to a non-student plan\n")
    return

def logout():
    print("Logging out...\n")

def title(text):
    print(bcolors.BOLD + bcolors.OKBLUE + "\n" + text + bcolors.ENDC)

def findAccountName(name):
    username = name.replace(" ", "")
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("_")
                name_section = "_".join(parts[1:-2])
                actual_name = name_section.rstrip("_")

                if actual_name.lower() == username.lower():
                    return True

        return False

    except FileNotFoundError:
        print("accounts.txt not found.")
        return False


menu = {
    1: ("Withdrawl", withdrawl),
    2: ("Transfer", transfer),
    3: ("Paybill", paybill),
    4: ("Deposit", deposit),
    5: ("Create Account", createAccount),
    6: ("Delete Account", deleteAccount),
    7: ("Disable Account", disableAccount),
    8: ("Changeplan", changeplan),
    9: ("Logout", logout)
}


#  Main menu loop
def main(session_type, name=None):
    logged_out = False
    while not logged_out:
        if name is not None:
            print("Logged In: " + bcolors.OKGREEN + name + bcolors.ENDC)

        display_map = {}
        display_num = 1
        print("\nEnter the number of the option you want to proceed with")
        if session_type == "standard":
            allowed_options = {1, 2, 3, 4, 9}
            for num, data in menu.items():
                name = data[0]
                if num in allowed_options:
                    display_map[display_num] = num
                    print(f"{display_num}. {name}")
                    display_num += 1
        elif session_type == "admin":
            for num, data in menu.items():
                name = data[0]
                display_map[display_num] = num
                print(f"{display_num}. {name}")
                display_num += 1
        else:
            errorMessage("Invalid session type.")

        try:
            choice = int(input("\nYour choice: "))
            if choice in display_map:
                actual_option = display_map[choice]
                title((menu[actual_option][0]).upper())
                if actual_option == 9:
                    logged_out = True
                    logout()
                else:
                    menu[actual_option][1](session_type)
            else:
                errorMessage("Invalid option.")
        except ValueError:
            print("Please enter a number.")


while True:
    title("Welcome to the Banking System")
    session_type = input("Enter session type (admin / standard) or 'quit' to end program: ").strip().lower()
    if session_type == "admin":
        main(session_type)
    elif session_type == "standard":
        name = input("Please enter your name with no spaces (ex: JohnDoe)\nor 'back' to return to main menu:\n")
        while True:
            if name.lower() == "back":
                break
            if findAccountName(name) is False:
                errorMessage("Account name not found. Please try again.\n")
                name = input("Please enter your name with no spaces (ex: JohnDoe)\nor 'back' to return to main menu:\n")
            else:
                main(session_type, name)
                break
    elif session_type == "quit":
        print("Exiting program.")
        break
    else:
        errorMessage("Invalid session type.")