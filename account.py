# Account class for account related functions
class Account:

    # Find account name functions
    def findAccountName(self, name):
        # Removing spaces from the name for comparison
        username = name.replace(" ", "")

        # Try catch to read accounts.txt file
        try:
            # While accounts.txt file is open, read each line one by one
            with open("accounts.txt", "r") as file:
                for line in file:
                    # Removing leading/trailing whitespace from the line
                    line = line.strip()

                    # Skipping empty lines
                    if not line:
                        continue

                    # Dividing account information
                    parts = line.split("_")
                    # Getting name section
                    name_section = "_".join(parts[1:-2])
                    # Removing underscores from name section
                    actual_name = name_section.rstrip("_")

                    # Checking if actual name matches the username (case insensitive)
                    if actual_name.lower() == username.lower():
                        return True
                    
                # If no name matches, return false
                return False
            
        # Throws errors if accounts.txt file is not found
        except FileNotFoundError:
            print("accounts.txt not found.")
            return False