from lib.greet import *

def test_greet_returns_hello_dave_for_dave():
    result = greet('Dave')
    assert result == 'Hello, Dave!'