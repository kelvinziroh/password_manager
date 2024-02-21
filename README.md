# Password Manager
Create or store, edit, delete and easily retrieve passwords to accounts from a linux command line
interface.

## Requirements
- python v3 or later
- pyperclip v1.8.2

## How it works
The program is implemented in python and has four main functionalities:
- Generate and store random passwords
- Edit passwords of specified account names
- Delete passwords of specified account names
- Retrieve any account's password to clipboard

On initial use of the program, a `stored_passwords.txt` file is automatically created with an empty dictionary in it. The Dictionary is the data structure used to store key-value pairs of each account and its corresponding password. The program is launched on the command line interface. It prompts the user for an account name, their preferred password length and automatically generates a password from a random selection of letters, digits and symbols of the user's preferred length. 

Editing a password for a specified account works the same way, only this time, the password of an existing account in the dictionary will be updated. Deleting a password record from the dictionary, *which should be done cautiously*, only prompts the user for the account name and the program will remove the key-value pair from the dictionary **permanently**.

Retrieving a password for a specified account also prompts a user for the account name and automatically copys the account's password from the dictionary to the clipboard enabling the user to simply paste the password wherever they use the password.

## How to use it
The pre-requisite requirements need to be fulfilled to run the program successfully preferably on a linux command line interface. The commands use options which are parsed as arguments which enable the program to behave differently with each option.

To get started, navigate to your preferred directory copy and paste the following command:
```
git clone git@github.com:kelvinziroh/password_manager.git
```
if you use a password-pretected ssh key.

or 

```
git clone https://github.com/kelvinziroh/password_manager.git
```
if you use the web URL.

To add a password of a specified account, run the following command:
```
python password_manager.py --add-password
```
The program will prompt the user for the account name and their preferred password length. It will automatically generate a password and store the password in the dictionary in the `stored_passwords.txt` file.

To edit a password of a specified account, run the following command:
```
python password_manager.py --edit-password
```
The program will prompt the user for the account name and their preferred password length. It will the overwrite the existing password linked to the specified account name.

To delete a password of a specified account, run the following command:
```
python password_manager.py --del-password
```
The program will prompt the user for the account name with a *WARNING* message reminding the user to be cautious while they proceed to delete an account's credentials. This will *permanently* remove the key-value pair from the dictionary.

To retrieve a password of a specified account, run the following command:
```
python password_manager.py --get-password
```
The program locates the password linked to the specified account in the dictionary and automatically copies the password to clipboard.

## Considerations
1. This simple program is only suitable for use locally as it is *insecure* and data in the `stored_passwords.txt` file could easily be lost. Hence a backup of the whole program with the file is highly recommended. 
2. You are more than welcome to modify the program to your liking and keep tracking the changes, hence remember to push the changes to a different remote repository. If you intend to use the program as it is, it's advisable to discard the .git directory from the working directory to stop tracking any changes that might take place as you read and write data in the `stored_passwords.txt` file. To remove the .git directory from the working directory simply navigate to the project's root directory and type in the following command:
```
rm -rf .git
```

## Acknowledgements
This is a slightly modified project from [Al Sweigart's](https://alsweigart.com/) book, [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) which is an excellent start for beginners who want to delve into the world of programming using the python programming language. 