import sys
from menu import Menu
from account import Account
# from utils import title, errorMessage


class Main:
    def __init__(self, accounts_file, transaction_file):
        self.accounts_file = accounts_file
        self.transaction_file = transaction_file
        self.account = Account(accounts_file)

    def start(self):

        # Open transaction file (writes fresh file each run)
        with open(self.transaction_file, "w") as trans_file:

            menu = Menu(trans_file)

            while True:
                print("Welcome to the Banking System")
                loginType = input(
                    "Enter session type (admin / standard) or 'quit' to end program: "
                ).strip().lower()

                if loginType == "admin":
                    menu.run(loginType)

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
                            menu.run(loginType, name)
                            break

                elif loginType == "quit":
                    print("Exiting program.")
                    break

                else:
                    print("Invalid session type.")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 main.py currentaccounts.txt transout.txt")
        sys.exit(1)

    accounts_file = sys.argv[1]
    transaction_file = sys.argv[2]

    app = Main(accounts_file, transaction_file)
    app.start()