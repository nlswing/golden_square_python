from lib.grammar_checker import *

"""
Given a text of empty words, the return would be False
"""

def test_empty_string_returns_false():
    result = grammar_checker("")
    assert result == False 
    
"""
Given a text that starts with a capital letter and ends with a full stop, the return would be True.
"""

def test_starts_with_capital_letter_ends_with_full_stop_returns_true():
    result = grammar_checker("This is a sentence.") 
    assert result == True
    
"""
Given a text that starts with a capital letter but does not end with valid punctuation, the return would be False.
"""

def test_starts_with_capital_but_does_not_end_with_valid_punctuation():
    result = grammar_checker("This is a sentence,") 
    assert result == False
    
"""
Given a text that starts with a capital letter and ends with another valid punctuation mark, the return would be True.
"""

def test_starts_with_capital_ends_with_exclam():
    result = grammar_checker("This is a sentence!") 
    assert result == True
    
"""
Given a text that starts with a lower-case letter, the return would be False.
"""

def test_text_starts_with_lower_case_letter():
    result = grammar_checker("this is a sentence.") 
    assert result == False