#! python3
# password_manager.py - An insecure password manager program

# Import necessary modules
import sys, pyperclip, argparse

# Store the passords for various accounts
PASSWORDS = {
    'email': ']"~9!k3-L.Lgj22)cMtp"`m/N3',
    'blog': 'j9J&-?FVk[jR;epaBpu&5$K7G#',
    'luggage': 'Fd,3<W"mebb!ZA!,r|6?)ytU!)',
}

# Create an argument parser
def get_arguments():
    parser = argparse.ArgumentParser(
        description='Manage passwords for different accounts'
    )

    # Add argument to the parser
    # Argument to add password to the manager
    parser.add_argument(
        '--add-password',
        action='store_true',
        help='Add a new password to the password manager'
    )

    # Argument to edit password in the manager
    parser.add_argument(
        '--edit-password',
        action='store_true',
        help='Edit an existing password in the password manager'
    )

    # Argument to delete an existing password in the manager
    parser.add_argument(
        '--del-password',
        action='store_true',
        help='Delete an existing password in the password manager'
    )
    
    return parser.parse_args()

# Parse the arguments
args = get_arguments()

# Add account to the password manager if it does not exist
def add_password(account_name, password):
    if account_name in PASSWORDS:
        print(
            f'{account_name} already exists in the password manager.')
    else:
        PASSWORDS[account_name] = password
        print(f'Password for {account_name} successfully added!')

# Edit account in the password manager if it exists
def edit_password(account_name, password):
    if account_name in PASSWORDS:
        PASSWORDS[account_name] = password
        print(f'Password for {account_name} successfuly updated!')
    else:
        print(
            f'{account_name} does not exist in the password manager.'
        )

# Delete account in the password manager if it exists
def del_password(account_name):
    if account_name in PASSWORDS:
        del PASSWORDS[account_name]
        print(f'Credentials for {account_name} successfully deleted!')
    else:
        print(
            f'{account_name} does not exist in the password manager.'
        )

# Prompt user for account credentials if add password argument has been used
if args.add_password:
    account = input('Account Name: ')
    password = input('Password: ')
    add_password(account, password)

# Prompt user for updated credentials if edit password argument has been used
if args.edit_password:
    account = input('Account name: ')
    password = input('Password: ')
    edit_password(account, password)

# Prompt user for account name if del password argument has been used
if args.del_password:
    warning_message = 'WARNING: You are about to permanently delete a record!'
    print(warning_message.center(len(warning_message) + 20, '-'))
    account = input('Account name: ')
    del_password(account)


# Alert user incase of invalid command line arguments
if len(sys.argv) < 2:
    print('Usage: python password_manager.py [account] - copy account password')
    sys.exit()

# Get the account name
account = sys.argv[1]

# Copy password if account name exists in stored passwords
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}.')