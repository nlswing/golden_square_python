from lib.check_todo import *

"""
Given a text of empty words, the return would be False
"""

def test_empty_string():
    result = check_todo("")
    assert result == False

"""
Given a text that includes the string #TODO, it will return True.
"""
def test_text_includes_correct_todo():
    result = check_todo("#TODO take the bins out.")
    assert result == True
    
"""
Given a text that does not include #TODO, it returns False.
"""
def test_text_does_not_include_todo():
    result = check_todo("Take bins out.")
    assert result == False
    
"""
Given a text that contains TODO, it would return False.
"""
def test_only_contains_TODO_no_hash():
    result = check_todo("Todo take bins out!")
    assert result == False
    
"""
Given a text that contains #todo, it returns False.
"""

def test_lower_case_correct_todo():
    result = check_todo("#todo take bins out.")
    assert result == False
    
"""
Given a text that just contains #TODO, it return True.
"""
def test_just_contains_correct_todo():
    result = check_todo("#TODO")
    assert result == True
