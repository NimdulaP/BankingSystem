# Banking System Application

# This program is a CLI program that allows users to perform banking operations such as withdrawal, 
# deposit, transfer, paybills, and account management (creating, deleting, disabling and changing account plans).
# It supports two types of sessions: admin and standard.
# Admin users have access to all operations, while standard users have limited access

# Files:
# currentaccounts.txt: Contains the current bank account information.
# /daily_transactions/dailytransactions{n}.txt: Directory that logs all transactions for each session.

# Testing Files:
# /inputs/in_{n}.txt: Contains the input for each test case.
# /expected_outputs/ex_{n}.txt: Contains the expected terminal output for each test case.
# /expected_outputs/ex_{n}.etf: Contains the expected daily transcation file for each test case.'
# /outputs/op_{n}.txt: Contains the actual terminal output for each test case.
# /outputs/op_{n}.atf: Contains the actual daily transcation file for each test case.

# Scripts:
# run_tests.sh: Script to run all test cases (macOS/Linux).
# run_tests.bat: Script to run all test cases (Windows).
# validate_tests.sh: Script to validate the test results by comparing actual outputs with expected outputs (macOS/Linux).
# validate_tests.bat: Script to validate the test results by comparing actual outputs with expected outputs (Windows).

# How to Run Test Scripts:
# MacOS/Linux:
#   chmod +x ./run_tests.sh
#   ./run_tests.sh
#   chmod +x ./validate_tests.sh 
#   ./validate_tests.sh 
# Windows:
#   .\run_tests.bat
#   .\validate_tests.bat

# How to Run Application:
# Execute the Application using Python 3:
#     python3 main.py
# Follow the prompts to log in as 'admin' or 'standard', perform transactions, 
# and logout to save the session's transactions.

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
                    if not self.account.find_account_name(name):
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