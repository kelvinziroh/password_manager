# Import the necessary modules
import pytest, password_manager, string


# Test the check_password_strength() function
def test_check_password_strength():
    assert password_manager.check_password_strength("MyStrongPassword123!") == True
    assert password_manager.check_password_strength("MyStrongPassword123") == False
    assert password_manager.check_password_strength("123!") == False
    assert password_manager.check_password_strength("MyStrongPassword") == False


# Test the read_from_shelf() function
@pytest.mark.parametrize("file_name", ["stored_passwords"])
def test_read_from_shelf(file_name):
    passwords = password_manager.read_from_shelf(file_name)
    assert isinstance(passwords, dict)


# Test the generate_password() function
# Test password lengths
@pytest.mark.parametrize("password_length", [8, 12, 16])
def test_generate_password_length(password_length):
    password = password_manager.generate_password(password_length)
    assert len(password) == password_length


# Test password characters
def test_generate_password_characters():
    password = password_manager.generate_password(12)
    assert any(char in string.ascii_letters for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)


# Test the get_arguments() function
# Test the --add-password argument from get_arguments()
def test_get_arguments_add_password():
    args = password_manager.get_arguments("--add-password".split())
    assert args.add_password is True
    assert args.edit_password is False
    assert args.del_password is False
    assert args.get_password is False


# Test the --edit-password argument from get_arguments()
def test_get_arguments_edit_password():
    args = password_manager.get_arguments("--edit-password".split())
    assert args.add_password is False
    assert args.edit_password is True
    assert args.del_password is False
    assert args.get_password is False


# Test the --del-password argument from get_arguments()
def test_get_arguments_del_password():
    args = password_manager.get_arguments("--del-password".split())
    assert args.add_password is False
    assert args.edit_password is False
    assert args.del_password is True
    assert args.get_password is False


# Test the --get-password argument from get_arguments()
def test_get_arguments_get_password():
    args = password_manager.get_arguments("--get-password".split())
    assert args.add_password is False
    assert args.edit_password is False
    assert args.del_password is False
    assert args.get_password is True
