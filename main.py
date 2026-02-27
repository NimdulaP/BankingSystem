import sys
from menu import Menu
from account import Account
# from utils import title, errorMessage


class Main:
    def __init__(self, accounts_file):
        self.accounts_file = accounts_file
        self.account = Account(accounts_file)
        self.menu = Menu()

    def start(self):

            while True:
                print("Welcome to the Banking System")
                loginType = input(
                    "Enter session type (admin / standard) or 'quit' to end program: "
                ).strip().lower()

                if loginType == "admin":
                    self.menu.run(loginType)

                elif loginType == "standard":
                    name = input(
                        "Please enter your name or 'back' to return to main menu:\n"
                    )

                    while True:
                        if name.lower() == "back":
                            break

                        if not self.account.findAccountName(name):
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
                    print("Exiting program.")
                    break

                else:
                    print("Invalid session type.")


if __name__ == "__main__":
    accounts_file = "currentaccounts.txt"

    app = Main(accounts_file)
    app.start()