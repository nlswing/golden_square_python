from lib.make_snippet import *

"""
Function returns a string that is passed as an argument.
"""

def test_returns_string_when_passed_as_argument():
    result = make_snippet('test')
    assert result == 'test'

"""
Words returned as when five words.
"""
    
def test_return_words_when_five_words():
    result = make_snippet('There are five words here')
    assert result == 'There are five words here'
    
"""
Words and '...' returned if more than five words in string
"""

def test_returns_words_and_dots_if_more_than_five():
    result = make_snippet('There are more than five words here')
    assert result == 'There are more than five...'

    

    
    