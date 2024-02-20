#! python3
# password_manager.py - An insecure password manager program

# Import necessary modules
import sys, pyperclip, argparse, ast, string, random


def read_from_file(file_name):
    try:
        # Get the file object and open it
        password_file = open(file_name)

        # Read the contents of the file object
        # Convert dictionary string to dictionary object
        return ast.literal_eval(password_file.read())
    except FileNotFoundError:
        # Create the file if it does not exist
        password_file = open(file_name, "w")
        password_file.write('{}')
        password_file.close()
        
        # Read the contents of the newly created file
        password_file = open(file_name)
        return ast.literal_eval(password_file.read())


def write_to_file(file_name, passwords_dict):
    # Overwrite password file contents
    stored_passwords = open(file_name, "w")
    stored_passwords.write(str(passwords_dict))
    stored_passwords.close()


# Create an argument parser
def get_arguments():
    parser = argparse.ArgumentParser(
        description="Manage passwords for different accounts"
    )

    # Add argument to the parser
    # Argument to add password to the manager
    parser.add_argument(
        "--add-password",
        action="store_true",
        help="Add a new password to the password manager",
    )

    # Argument to edit password in the manager
    parser.add_argument(
        "--edit-password",
        action="store_true",
        help="Edit an existing password in the password manager",
    )

    # Argument to delete an existing password in the manager
    parser.add_argument(
        "--del-password",
        action="store_true",
        help="Delete an existing password in the password manager",
    )

    # Argument to copy password in the manager
    parser.add_argument(
        "--get-password",
        action="store_true",
        help="Copy the password for the corresponding account in the manager",
    )

    return parser.parse_args()


# Generate random passwords
def generate_password(password_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to construct the password
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password


# Add account to the password manager if it does not exist
def add_password(account_name, password):
    # Get passwords from password file
    PASSWORDS = read_from_file("stored_passwords.txt")

    if account_name in PASSWORDS:
        print(f"{account_name} already exists in the password manager.")
    else:
        PASSWORDS[account_name] = password

        # Overwrite password file contents
        write_to_file("stored_passwords.txt", PASSWORDS)

        # Alert user that password has successfully been added
        print(f"Password for {account_name} successfully added!")


# Edit account in the password manager if it exists
def edit_password(account_name, password):
    # Get passwords from password file
    PASSWORDS = read_from_file("stored_passwords.txt")
    if account_name in PASSWORDS:
        PASSWORDS[account_name] = password

        # Overwrite password file contents
        write_to_file("stored_passwords.txt", PASSWORDS)

        # Alert user that password has successfully been updated
        print(f"Password for {account_name} successfuly updated!")
    else:
        print(f"{account_name} does not exist in the password manager.")


# Delete account in the password manager if it exists
def del_password(account_name):
    # Get passwords from password file
    PASSWORDS = read_from_file("stored_passwords.txt")
    if account_name in PASSWORDS:
        del PASSWORDS[account_name]

        # Overwrite password file contents
        write_to_file("stored_passwords.txt", PASSWORDS)

        # Alert user that password has successfully been deleted
        print(f"Credentials for {account_name} successfully deleted!")
    else:
        print(f"{account_name} does not exist in the password manager.")


# Copy account's password if it exists in the password manager
def get_password(account_name):
    # Get passwords from password file
    PASSWORDS = read_from_file("stored_passwords.txt")
    if account_name in PASSWORDS:
        pyperclip.copy(PASSWORDS[account_name])
        print(f"Password for {account_name} copied to clipboard!")
    else:
        print(f"{account_name} does not exist in the password manager.")


def main():
    # Parse the arguments
    args = get_arguments()

    # Alert user incase of invalid command line arguments
    if len(sys.argv) < 2:
        print("Usage: python password_manager.py [account] - copy account password")
        sys.exit()

    # Prompt user for account credentials if add password argument has been used
    if args.add_password:
        account = input("Account name: ")
        password_length = int(input("Password length: "))
        password = generate_password(password_length)
        add_password(account, password)

    # Prompt user for updated credentials if edit password argument has been used
    if args.edit_password:
        account = input("Account name: ")
        password_length = int(input("Password length: "))
        password = generate_password(password_length)
        edit_password(account, password)

    # Prompt user for account name if del password argument has been used
    if args.del_password:
        warning_message = "WARNING: You are about to permanently delete a record!"
        print(warning_message.center(len(warning_message) + 20, "-"))
        account = input("Account name: ")
        del_password(account)

    # Prompt user for account name if get password argument has been used
    if args.get_password:
        account = input("Account name: ")
        get_password(account)


if __name__ == "__main__":
    main()
