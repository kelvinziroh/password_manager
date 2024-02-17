#! python3
# password_manager.py - An insecure password manager program

# Import necessary modules
import sys, pyperclip, argparse

# Create an argument parser
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

# Create different commands for different use cases
# Prompt the user for account name and password
# Add account and password if account doesn't exist
# Copy password if account name exists in stored passwords

# Store the passords for various accounts
PASSWORDS = {
    'email': ']"~9!k3-L.Lgj22)cMtp"`m/N3',
    'blog': 'j9J&-?FVk[jR;epaBpu&5$K7G#',
    'luggage': 'Fd,3<W"mebb!ZA!,r|6?)ytU!)',
}

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