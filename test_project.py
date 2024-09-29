import pytest, project, string

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