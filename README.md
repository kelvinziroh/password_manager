# Password Manager
### Video Demo: click [here]()


### Description
Add, retrieve, edit and delete passwords to different accounts from a linux command line interface.

## Acknowledgements
This project was undertaken in partial fulfillment of the requirements on [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022). It draws inspiration from [Al Sweigart's](https://alsweigart.com/) book, [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/). 


## Project Files
- `project.py`
    1. Imports necessary modules required for the program to run successfully. 
    2. It then implements the password management functionality using the main and helper functions. The helper functions modularize specific steps to be taken when the program runs and implement the necessary password functionality. The main function simply checks the command-line arguments passed when the program is run on the terminal and calls the appropriate helper functions based on the command-line argument captured. 
- `test_project.py`
    1. Imports the **pytest** framework, the project module along with any other necessary libraries for the tests to run successfully.
    2. Runs tests to some of the helper functions defined in the main project module to ensure they run as required.
- `README.md` - Contains documentation on how to the program works and how to use it.
- `stored_passwords.db` - Shelve file that contains the stored passwords.
- `requirements.txt` - A plain text file with information on necessary `pip`-installable packages necessary for the program to work.
- `.gitignore` - A plain text file that mentions files to be ignored by the git version control system.

## How it works
This python implementation of a password manager has four main **(CRUD)** functionalities:
- **Create**: Generate and store random passwords
- **Read**: Retrieve any account's password to clipboard
- **Update**: Edit passwords of specified account names
- **Delete**: Delete passwords of specified account names

The python script runs on a linux command line interface and persists the passwords data into a shelve file i.e `stored_passwords.db`. As specified above, the program allows a user to add, retrieve, edit and delete passwords from the shelf file. 

The data structure used in storing the data is the python **dictionary** which stores key-value pairs of each account and their corresponding passwords. To perform different actions as the script is run on the terminal, the program uses options or command line arguments i.e `--add-password` for adding passwords, `--get-password` for retrieving passwords to clipboard, `--edit-password` for updating existing passwords and `--del-password` for removing passwords.  

**Creating/Adding** a password for a specified account prompts the user for an `account name`, their preferred `password length` and automatically generates a password from a random selection of letters, digits and symbols. To create strong passwords, the program restricts the user to enter `password length`s of at least 8 characters. It then regenerates different character combinations until the password combination has at least one occurence of each type of character i.e *letters, digits* and *punctuation symbols*. 

**Retrieving** a password for a specified account prompts the user for the `account name` and automatically copys the account's password from the dictionary to the clipboard enabling the user to simply paste the password wherever they use the password eliminating the need to remember and type in multiple passwords to different accounts.

**Editing** a password for a specified account works the same way as adding a password does, only this time, the password of an *existing* account in the dictionary will be updated. If the typed account name does not exist in the shelve file, a message will be printed to that effect and the program will terminate.

**Deleting** a password record from the dictionary, *which should be done cautiously*, only prompts the user for the `account name` and the program will remove the key-value pair from the dictionary **permanently**.

## How to use it
The pre-requisite requirements need to be fulfilled to run the program successfully preferably on a linux command line interface. This project was built in a `conda` environment but even a `venv` will suffice. The commands use options/command line arguments which are parsed as arguments in the python script and enable the program to behave differently depending on the option captured when the program is run by the user on the terminal.

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

You should have the project files downloaded to the current working directory. You can then initialize a python `venv` or a `conda` environment in which you can install the necessary packages listed in the `requirements.txt` file.

Also feel free to delete the `.git` repository which will track changes made to the `stored_passwords.db` shelve file as you write data into it while creating and updating passwords into the shelve file. Just run the following command to do so:
```
rm -rf .git
```

Due to the requirements of the project's submission, the script with the main password management functionality is named `project.py`. However to follow along with the tutorial below on how to use the program, feel free to rename the file to `password_manager.py` by running the following command:
```
mv project.py password_manager.py
```

To **add** a password of a specified account, run the following command:
```
python password_manager.py --add-password
```
The program will prompt the user for the `account name` and their preferred `password length`. It will keep prompting the user for a length of at least 8 characters long. Once the acceptable password length criteria is satisfied, it will automatically generate a password, store it in a dictionary and persist it into the `stored_passwords.db` shelve file. If such an `account name` already exists in the shelve file, a message will be printed to that effect and the program will terminate.

To **retrieve** a password of a specified account, run the following command:
```
python password_manager.py --get-password
```
The program prompts the user for the `account name` and automatically copies the password associated to the specified account to clipboard. If the `account name` does not exist in the shelve file, then a message will be printed to that effect and the program will terminate.

To **edit** a password of a specified account, run the following command:
```
python password_manager.py --edit-password
```
The program will prompt the user for the `account name` and their preferred `password length`. It will then overwrite the existing password linked to the specified `account name`. If the specified `account name` does not exist in the shelve file, a message is printed to that effect and the program terminates.

To **delete** a password of a specified account, run the following command:
```
python password_manager.py --del-password
```
The program will prompt the user for the `account name` with a *WARNING* message reminding the user to be cautious while they proceed to delete an account's credentials. This will *permanently* remove the key-value pair from the dictionary. As with the other functionalities, if the mentioned `account name` does not exist, a message is printed to that effect and the program terminates.

> **NOTE**: To exit any of the prompts, simply hit `CTRL + C` which will raise a `KeyboardInterrupt Exception` and therefore exit the program.

## Considerations
This simple program was built as a classroom project hence was not built with password security features in mind and as such is only suitable for use locally as it is *not secure* and data in the `stored_passwords.db` file could easily be lost. Hence a backup of the whole program with the shelve file is highly recommended. 