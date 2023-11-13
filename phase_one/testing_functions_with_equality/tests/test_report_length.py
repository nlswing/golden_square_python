from lib.report_length import *

def test_string_is_eight_chars_long():
    result = report_length('makersac')
    assert result  == "This string was 8 characters long."
    
def test_string_is_zero_chars_long():
    result = report_length('')
    assert result  == "This string was 0 characters long."