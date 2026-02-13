# Source - https://stackoverflow.com/a/287944
# Posted by joeld, modified by community
# Retrieved 2026-02-12, License - CC BY-SA 4.0
# Coloured text class
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

# Error message function
def errorMessage(message):
    # Dislaying error message in red text
    print(bcolors.FAIL + message + bcolors.ENDC)

# Title function
def title(text):
    # Displaying title in bold blue text
    print(bcolors.BOLD + bcolors.OKBLUE + "\n" + text + bcolors.ENDC)