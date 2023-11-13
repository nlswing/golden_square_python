import pytest
from lib.password_checker import *

"""
Throws exception if password is invalid.
"""

def test_invalid_password_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('pass')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    
"""
Returns True when valid password is given.
"""

def test_valid_password():
    password_checker = PasswordChecker()
    result = password_checker.check('password123')
    assert result == True
    