from lib.counter import *

"""
Initially reports a count of zero
"""
def test_no_number_added_to_counter():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."
    
"""
When we add a single number it is reflected in final count.
This is testing ALL the methods but is not testing BEHAVIOUR effectively.
"""
    
def test_one_number_added_to_counter():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."
    
"""
When we add a two numbers it is reflected in final count
This is testing the BEHAVIOUR of the class.
"""

def test_two_numbers_added_to_counter():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."