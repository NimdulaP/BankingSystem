# Importing classes and functions
from menu import Menu
from account import Account
from utils import title, errorMessage

# Main class to run application
class main:
    def __init__(self):
        # Initialzing menu and account variables
        self.menu = Menu()
        self.account = Account()

    def start(self):
        # Main loop for the system  
        while True:
            title("Welcome to the Banking System")
            # Getting user's session type
            loginType = input("Enter session type (admin / standard) or 'quit' to end program: ").strip().lower()

            # Checking if user is admin or standard
            if loginType == "admin":
                self.menu.run(loginType)

            elif loginType == "standard":
                # Getting username
                name = input("Please enter your name or 'back' to return to main menu:\n")
                while True:
                    # Validating username
                    if name.lower() == "back":
                        break
                    if not self.account.findAccountName(name):
                        errorMessage("Account name not found. Please try again.\n")
                        name = input("Please enter your name or 'back' to return to main menu:\n")
                    else:
                        self.menu.run(loginType, name)
                        break
            # Quitting program
            elif loginType == "quit":
                print("Exiting program.")
                break
            else:
                errorMessage("Invalid session type.")

if __name__ == "__main__":
    # Running the application
    app = main()
    app.start()