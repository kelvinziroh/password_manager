#! python3
# password_manager.py - An insecure password manager program

# Import necessary modules
import sys

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

