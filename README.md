# Password Manager
Add, retrieve, edit and delete passwords to different accounts from a linux command line interface.

## Acknowledgements
This project draws inspiration from [Al Sweigart's](https://alsweigart.com/) book, [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) which is an excellent resource for beginners who want to delve into the world of programming using the python programming language.

## Requirements
- python v3 or later
- pyperclip v1.8.2

## How it works
This python implementation of a password manager has four main **(CRUD)** functionalities:
- **Create**: Generate and store random passwords
- **Read**: Retrieve any account's password to clipboard
- **Update**: Edit passwords of specified account names
- **Delete**: Delete passwords of specified account names

The python script runs on a linux command line interface and persists the passwords data into a shelf file i.e `stored_passwords.db`. As specified above, the program allows a user to add, retrieve, edit and delete passwords from the shelf file. The data structure used in storing the data is the python **dictionary** which stores key-value pairs of each account and their corresponding passwords. To perform different actions as the script is run on the terminal, the program uses options i.e `--add-password` for adding passwords, `--get-password` for retrieving passwords to clipboard, `--edit-password` for updating existing passwords and `--del-password` for removing passwords.  

**Adding** a password for a specified account prompts the user for an `account name`, their preferred `password length` and automatically generates a password from a random selection of letters, digits and symbols. 

**Getting** a password for a specified account prompts the user for the `account name` and automatically copys the account's password from the dictionary to the clipboard enabling the user to simply paste the password wherever they use the password.

**Editing** a password for a specified account works the same way as adding a password does, only this time, the password of an *existing* account in the dictionary will be updated. 

**Deleting** a password record from the dictionary, *which should be done cautiously*, only prompts the user for the `account name` and the program will remove the key-value pair from the dictionary **permanently**.

## How to use it
The pre-requisite requirements need to be fulfilled to run the program successfully preferably on a linux command line interface. The commands use options which are parsed as arguments and enable the program to behave differently with each option.

Assuming you have the git version control system installed locally, navigate to your preferred directory copy and paste the following command:
```
git clone git@github.com:kelvinziroh/password_manager.git
```
if you use a password-pretected ssh key.

or 

```
git clone https://github.com/kelvinziroh/password_manager.git
```
if you use the web URL.

To **add** a password of a specified account, run the following command:
```
python password_manager.py --add-password
```
The program will prompt the user for the `account name` and their preferred `password length`. It will automatically generate a password and store the password in the dictionary and persist it into the `stored_passwords.db` shelf file.

To **retrieve** a password of a specified account, run the following command:
```
python password_manager.py --get-password
```
The program prompts the user for the `account name` and automatically copies the password associated to the specified account to clipboard.

To **edit** a password of a specified account, run the following command:
```
python password_manager.py --edit-password
```
The program will prompt the user for the `account name` and their preferred `password length`. It will then overwrite the existing password linked to the specified `account name`.

To **delete** a password of a specified account, run the following command:
```
python password_manager.py --del-password
```
The program will prompt the user for the `account name` with a *WARNING* message reminding the user to be cautious while they proceed to delete an account's credentials. This will *permanently* remove the key-value pair from the dictionary.

> **NOTE**: To exit any of the prompts, simply hit `CTRL + C` which will raise a `KeyboardInterrupt Exception` and therefore exit the program.

## Considerations
1. This simple program is only suitable for use locally as it is *not secure* and data in the `stored_passwords.db` file could easily be lost. Hence a backup of the whole program with the shelf file is highly recommended. 
2. If you intend to use the program as it is, it's advisable to discard the `.git` directory from the working directory to stop tracking any changes that might take place as you read and write data to and from the `stored_passwords.db` file. To remove the `.git` directory from the working directory simply navigate to the project's root directory and run `rm -rf .git` and you should be good to go 😎.