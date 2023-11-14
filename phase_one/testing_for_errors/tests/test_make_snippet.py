from lib.make_snippet import *

"""
Function returns a string that is passed as an argument.
"""

def test_returns_string_when_passed_as_argument():
    result = make_snippet('test')
    assert result == 'test'
