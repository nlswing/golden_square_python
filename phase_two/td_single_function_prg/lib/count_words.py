from lib.count_words import *

"""
Returns 0 for an empty string.
"""

def test_returns_zero_for_empty_string():
    result = count_words("")
    assert result == 0