from lib.string_builder import *

"""
Empty string
"""
def test_no_string_added():
    stringBuilder = StringBuilder()
    result_of_length = stringBuilder.size()
    assert result_of_length == 0
    result_of_str = stringBuilder.output()
    assert result_of_str == ""
    
"""
When string is added, length is returned and string is added succesfully
"""

def test_one_string_added():
    stringBuilder = StringBuilder()
    stringBuilder.add("hello")
    result_of_length = stringBuilder.size()
    # Try not to do more than one assert. Test individual behaviour. Makes in more difficult to narrow down where the failure is.
    assert result_of_length == 5
    result_of_str = stringBuilder.output()
    assert result_of_str == "hello"
    
def test_length_of_one_string():
    stringBuilder = StringBuilder()
    stringBuilder.add("hello")
    result_of_length = stringBuilder.size()
    assert result_of_length == 5
    
def test_multiple_strings_are_added_and_concatenated():
    stringBuilder = StringBuilder()
    stringBuilder.add("hello")
    stringBuilder.add("world")
    result_of_str = stringBuilder.output()
    assert result_of_str == "helloworld"
    
def test_string_has_blank_space():
    stringBuilder = StringBuilder()
    stringBuilder.add('Hello World')
    result_of_length = stringBuilder.size()
    assert result_of_length == 11
    