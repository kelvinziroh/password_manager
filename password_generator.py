# Import necessary modules
import argparse
import random
import string

# Create an argument parser
parser = argparse.ArgumentParser(
    description='Generate random passwords of specified length.')

# Add arguments to the parser
parser.add_argument(
    'length',
    type=int,
    help='The desired length of the password.'
)

parser.add_argument(
    '--include-symbols',
    action='store_true',
    help='Add symbols to the generated password.'
)

parser.add_argument(
    '--exclude-similar',
    action='store_true',
    help='Exclude similar looking characters (e.g., l, 1, I).'
)

# Get the arguments
args = parser.parse_args()

# Construct a string of characters using ascii letters and digits
characters = string.ascii_letters + string.digits

# Add punctuation symbols if the --include-symbols option is part of the arguments
if args.include_symbols:
    characters += string.punctuation

# Remove similar looking characters if the --exclude-similar option is part of the arguments
if args.exclude_similar:
    similar_characters = 'oO0l1I'
    characters = ''.join(c for c in characters if c not in similar_characters)

# Randomly select characters to construct the password of specified length
password = ''.join(random.choice(characters) for _ in range(args.length))

# Print out the password
print(password)