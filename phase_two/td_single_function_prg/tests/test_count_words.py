from lib.count_words import *

"""
Returns 0 for an empty string.
"""

def test_returns_zero_for_empty_string():
    result = count_words("")
    assert result == 0
    
"""
Returns 1 for a string that contains one word.
"""

def test_returns_one_for_one_word_string():
    result = count_words('word')
    assert result == 1
    
"""
Returns 5 for a string that contains 5 words.
"""

def test_returns_five_for_string_of_five_words():
    result = count_words('This is five words long.')
    assert result == 5

"""
Returns 100 for a 100 word string.
"""   

def test_returns_one_hundered_for_one_hundred_word_string():
    result = count_words('hello ' * 100)
    assert result == 100