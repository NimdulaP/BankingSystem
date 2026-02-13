# Importing classes and functions
from transactions import Transactions
from utils import errorMessage, title, bcolors

# Menu class to list options and run transactions
class Menu:
    def __init__(self):
        # Initizalizing transaction and menu variable
        self.operations = Transactions()
        self.menu = {
            1: ("Withdrawal", self.operations.withdrawal),
            2: ("Transfer", self.operations.transfer),
            3: ("Paybill", self.operations.paybill),
            4: ("Deposit", self.operations.deposit),
            5: ("Create Account", self.operations.createAccount),
            6: ("Delete Account", self.operations.deleteAccount),
            7: ("Disable Account", self.operations.disableAccount),
            8: ("Changeplan", self.operations.changeplan),
            9: ("Logout", self.logout)
        }

    # Logout function
    def logout(self):
        print("Logging out...\n")

    # Display and run transactions function
    def run(self, loginType, name=None):
        loggedOut = False

        # Listing each option until user logs out
        while not loggedOut:

            # Displaying username (if given)
            if name is not None:
                print("Logged In: " + bcolors.OKGREEN + name + bcolors.ENDC)

            # Creating the list of allowed options
            displayMap = {}
            displayNum = 1

            # Listing options based on session type
            print("\nEnter the number of the option you want to proceed with")
            if loginType == "standard":
                # Only lists options 1-4 & 9 for standard users
                allowedOptions = {1, 2, 3, 4, 9}
                for num, data in self.menu.items():
                    optionName = data[0]
                    if num in allowedOptions:
                        # Displaying and mapping options
                        displayMap[displayNum] = num
                        print(f"{displayNum}. {optionName}")
                        displayNum += 1
            elif loginType == "admin":
                # Lists all options for admins
                for num, data in self.menu.items():
                    optionName = data[0]
                    displayMap[displayNum] = num
                    # Displaying and mapping options
                    print(f"{displayNum}. {optionName}")
                    displayNum += 1
            else:
                # Displaying error message for session types not standard nor admin
                errorMessage("Invalid session type.")

            # Try catch to get only valid options
            try:
                # Getting user's transaction option
                choice = int(input("\nYour choice: "))
                if choice in displayMap:
                    # If the option is valid and allowed, run the transaction
                    actualOption = displayMap[choice]
                    title((self.menu[actualOption][0]).upper())
                    # Logging out if the user selects logout transaction
                    if actualOption == 9:
                        loggedOut = True
                        self.logout()
                    # Standard transactions require session type and name, while admin transactions only require session type
                    elif actualOption >= 5 and actualOption <= 8:
                        self.menu[actualOption][1](loginType)
                    else:
                        self.menu[actualOption][1](loginType, name)
                else:
                    # Displaying error message if option selected isn't listed
                    errorMessage("Invalid option.")
            except ValueError:
                # Displaying error message if user's input isn't a number
                print("Please enter a number.")