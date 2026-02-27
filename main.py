from menu import Menu
from account import Account

# Main class to run the program
class Main:
    def __init__(self, accountsFile):
        # Initialize the accounts file and create an Account object and Menu object
        self.accountsFile = accountsFile
        self.account = Account()
        self.menu = Menu()

    def start(self):
        # Main loop to run the program until user quits 
        while True:
            print("Welcome to the Banking System")
            loginType = input(
                "Enter session type (admin / standard) or 'quit' to end program: "
            ).strip().lower()
            # Run the menu for admin sessions
            if loginType == "admin":
                self.menu.run(loginType)
            # Else, if the user selects standard, ask for their name
            elif loginType == "standard":
                name = input(
                    "Please enter your name or 'back' to return to main menu:\n"
                )
                
                # Loop until the user enters a valid name or chooses to go back to the main menu
                while True:
                    if name.lower() == "back":
                        break

                    # Check if the entered name exists in the accounts file
                    if not self.account.findAccountName(name):
                        # If not, display an error message and prompt the user to enter their name again or go back to the main menu
                        print(
                            "Account name not found. Please try again.\n"
                        )
                        name = input(
                            "Please enter your name or 'back' to return to main menu:\n"
                        )
                    else:
                        self.menu.run(loginType, name)
                        break
            elif loginType == "quit":
                # If the user selects quit, end the program
                print("Exiting program.")
                break

            else:
                # Display error message if the user enters an invalid session type
                print("Invalid session type.")


if __name__ == "__main__":
    # Initialize the accounts file and start the program
    accountsFile = "currentaccounts.txt"
    app = Main(accountsFile)
    app.start()