import pytest
from lib.diary import Diary

'''
Diary intially returns an empty list.
'''

def test_diary_returns_empty_list():
    diary = Diary()
    assert diary.all() == []
    
'''
Initally word count is zero. 
'''

def test_intial_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0
    
'''
Initally, #reading_time should raise an error
'''

def test_intially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet."
    
'''
Initially, #find_best_entry_for_reading_time should raise and error
'''

def test_initally_find_best_entry_for_reading_time_should_raise_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2, 2)
    assert str(err.value) == 'No entries added yet.'
