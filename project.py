#! python3
# password_manager.py - A local command-line based password manager program

# Import necessary modules
import sys, pyperclip, argparse, string, random, shelve


def read_from_shelf(file_name):
    try:
        # Open the shelf file object
        password_file = shelve.open(file_name)
        # Get the passwords dictionary data
        password_dict = password_file["passwords"]
        # close the shelf file
        password_file.close()
        # Return the password dictionary
        return password_dict
    except KeyError:
        # Create an empty dictionary
        new_dict = {}
        # Open the shelf file object
        password_file = shelve.open(file_name)
        # Assisgn the empty dictionary to the password file
        password_file["passwords"] = new_dict
        # Get the passwords dictionary data
        password_dict = password_file["passwords"]
        # Close the shelf file
        password_file.close()
        # Return the password dictionary
        return password_dict


def write_to_shelf(file_name, passwords_dict):
    # retrieve passwords from the shelf file
    stored_passwords = shelve.open(file_name)
    stored_passwords["passwords"] = passwords_dict
    stored_passwords.close()


# Create an argument parser
def get_arguments(args=None):
    """
    Define and parse arguments typed in by the user to determine the program's
    functionality during runtime

    Args:
    args: Optional, list of strings to parse as arguments during unit tests

    Returns:
    Parsed arguments
    """
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

    return parser.parse_args(args)


# Generate random passwords
def generate_password(password_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to construct the password
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password


def add_password(account_name, password):
    # Get the passwords dictionary from the shelf file
    PASSWORDS = read_from_shelf("stored_passwords")
    # Specify the data to be persisted
    PASSWORDS[account_name] = password
    # persist the data to the shelf file
    write_to_shelf("stored_passwords", PASSWORDS)
    # Alert user of successful password addition
    print(f"Password for {account_name} successfully added!")


# Edit account in the password manager if it exists
def edit_password(account_name, password):
    # Get passwords from password file
    PASSWORDS = read_from_shelf("stored_passwords")
    if account_name in PASSWORDS:
        PASSWORDS[account_name] = password

        # Overwrite password file contents
        write_to_shelf("stored_passwords", PASSWORDS)

        # Alert user that password has successfully been updated
        print(f"Password for {account_name} successfuly updated!")
    else:
        print(f"{account_name} does not exist in the password manager.")


# Delete account in the password manager if it exists
def del_password(account_name):
    # Get passwords from password file
    PASSWORDS = read_from_shelf("stored_passwords")
    if account_name in PASSWORDS:
        del PASSWORDS[account_name]

        # Overwrite password file contents
        write_to_shelf("stored_passwords", PASSWORDS)

        # Alert user that password has successfully been deleted
        print(f"Credentials for {account_name} successfully deleted!\n")
    else:
        print(f"{account_name} does not exist in the password manager.")


# Copy account's password if it exists in the password manager
def get_password(account_name):
    # Get passwords from password file
    PASSWORDS = read_from_shelf("stored_passwords")
    if account_name in PASSWORDS:
        pyperclip.copy(PASSWORDS[account_name])
        print(f"Password for {account_name} copied to clipboard!")
    else:
        print(f"{account_name} does not exist in the password manager.")


# Display the account names in the stored passwords file
def display_accounts():
    # Display a message
    message = "Stored Account passwords"
    print("=" * (len(message) + 20))
    print(message.center(len(message) + 20))
    print("=" * (len(message) + 20))
    # Get passwords from the password file
    PASSWORDS = read_from_shelf("stored_passwords")
    for account in PASSWORDS.keys():
        print(f"- {account}")


def main():
    # Parse the arguments
    args = get_arguments()

    # Alert user incase of invalid command line arguments
    if len(sys.argv) < 2:
        print(
            "Usage: python password_manager.py [--option] - Generate, add, edit and delete passwords to accounts"
        )
        sys.exit()

    # Prompt user for account credentials if add password argument has been used
    if args.add_password:
        # Display the accounts available in the stored passwords
        display_accounts()
        try:
            account = input("\nAccount name: ")
            password_length = int(input("Password length: "))
            password = generate_password(password_length)
            add_password(account, password)
        except KeyboardInterrupt:
            sys.exit("\nPassword creation successfully cancelled!")

    # Prompt user for updated credentials if edit password argument has been used
    if args.edit_password:
        # Display the accounts available in the stored passwords
        display_accounts()
        try:
            account = input("\nAccount name: ")
            password_length = int(input("Password length: "))
            password = generate_password(password_length)
            edit_password(account, password)
        except KeyboardInterrupt:
            sys.exit("\nPassword update successfully cancelled!")

    # Prompt user for account name if del password argument has been used
    if args.del_password:
        warning_message = "WARNING: You are about to permanently delete a record!"
        # Display the accounts available in the stored passwords
        display_accounts()
        try:
            print(f"\n{warning_message}")
            account = input("Account name: ")
            del_password(account)
            display_accounts()
        except KeyboardInterrupt:
            sys.exit("\nPassword deletion successfully cancelled!")

    # Prompt user for account name if get password argument has been used
    if args.get_password:
        # Display the accounts available in the stored passwords
        display_accounts()
        try:
            account = input("\nAccount name: ")
            get_password(account)
        except KeyboardInterrupt:
            sys.exit("\nPassword retrieval successfully cancelled!")


if __name__ == "__main__":
    main()
