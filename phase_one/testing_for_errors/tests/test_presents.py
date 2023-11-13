import pytest
from lib.present import *

"""
Throws exceptions if no contents have been wrapped.
"""

def test_nothing_wrapped_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    
"""
Throws exception if a contents has already been wrapped.
"""

def test_contents_already_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap('golf set')
        present.wrap('socks')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    
"""
Contents is wrapped and unwrapped.
"""

def test_contents_is_wrapped_and_unwrapped():
    present = Present()
    present.wrap('socks')
    result = present.unwrap()
    assert result == 'socks'
    
    
