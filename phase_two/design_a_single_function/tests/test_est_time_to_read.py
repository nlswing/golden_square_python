import pytest
from lib.est_time_to_read import *

"""
Given a text of empty words, time to read would be 0.
"""

def test_list_of_empty_words():
    result = est_reading_time("")
    assert result == 0
    
"""
Given a text of 200 words, time to read would be 1.
"""

def test_text_of_200_words():
    result = est_reading_time("Hello " * 200)
    assert result == 1
    
"""
Given a text of 150 words, time to read would be 1.
"""

def test_text_of_150_words():
    result = est_reading_time("Hello " * 150) 
    assert result == 1

"""
Given a text of 400 words, time to read would be 2.
"""
def test_text_of_400_words():
    result = est_reading_time("Hello " * 400)
    assert result == 2
    
"""
Given a text of 25,000 words, time to read would 
"""

def test_text_of_many_words():
    result = est_reading_time("Hello " * 25000) 
    assert result == 125
    
"""
Given a text that uses punctuation, only words are counted.

"""
def test_text_of_words_with_punctuation():
    result = est_reading_time("Hello, ! " * 200) 
    assert result == 1

"""
Given a text that is not a string type. An error is thrown.
"""

def test_text_is_not_string_error_thrown():
    with pytest.raises(Exception) as e:
        est_reading_time(None) 
    error_message = str(e.value)
    assert error_message == "Invalid input. Please use a text of string type"