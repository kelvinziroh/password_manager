import pytest, project, string, argparse

# Test password lengths
@pytest.mark.parametrize("password_length", [8, 12, 16])
def test_generate_password_length(password_length):
    password = project.generate_password(password_length)
    assert len(password) == password_length

# Test password characters
def test_generate_password_characters():
    password = project.generate_password(12)
    assert any(char in string.ascii_letters for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

# Test the --add-password argument from get_arguments()
def test_get_arguments_add_password():
    args = project.get_arguments("--add-password".split())
    assert args.add_password is True
    assert args.edit_password is False
    assert args.del_password is False
    assert args.get_password is False

# Test the --edit-password argument from get_arguments()
def test_get_arguments_edit_password():
    args = project.get_arguments("--edit-password".split())
    assert args.add_password is False
    assert args.edit_password is True
    assert args.del_password is False
    assert args.get_password is False