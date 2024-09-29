import pytest, project

# Test password lengths
@pytest.mark.parametrize("password_length", [8, 12, 16])
def test_generate_password_length(password_length):
    password = project.generate_password(password_length)
    assert len(password) == password_length