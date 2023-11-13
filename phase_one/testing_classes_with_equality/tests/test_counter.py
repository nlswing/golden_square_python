from lib.counter import *

def test_no_number_added_to_counter():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."
    
def test_one_number_added_to_counter():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_two_numbers_added_to_counter():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."