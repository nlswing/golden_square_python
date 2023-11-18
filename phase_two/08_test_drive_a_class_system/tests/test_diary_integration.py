from lib.diary import Diary
from lib.diary_entry import DiaryEntry

''' 
Returns a list of diary entries.
'''
def test_returns_list_of_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'my entry 1')
    entry_2 = DiaryEntry('my title 2', 'my entry 2')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]
    
'''
Returns a number repesenting the number of words in all diary entries.
'''

def test_returns_sum_of_words_in_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'here are some contents')
    entry_2 = DiaryEntry('my title 2', 'here are some more contents')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 9

    

'''
Given I add two diary entries with a total length of 10
And I call #reading_time with a wpm of 2
Then the total reading time should be 5
'''

def test_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'here are some contents')
    entry_2 = DiaryEntry('my title 2', 'here are some more contents again')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 5



'''
Given I add two diary entries, one lond and one short
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can only read the short one
The #find_best_entry_for_reading_time returns the shorter one
'''

def test_returns_best_diary_entry_in_given_time():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'here is some contents')
    entry_2 = DiaryEntry('my title 2', 'here are some more contents again do you see')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1
    
    
'''
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can read that entry
Then #find_best_entry_for_reading_time returns that entry
'''

def test_find_best_entry_for_reading_time_returns_single_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'contents are here')
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1
    
''' 
Given I add a diary entry
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I cannot read that entry
Then #find_best_entry_for_reading_time returns None
'''

def test_find_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'contents are here and there are more words here than can be read')
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None
    
'''
Given I add two diary entries
And I call #find_best_entry_for_reading_time
With a wpm and minutes that mean I could read both
Then #find_best_entry_for_reading_time_returns_the_longer_one
'''

def test_find_best_entry_for_reading_time_returns_the_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry('my title 1', 'here is some contents')
    entry_2 = DiaryEntry('my title 2', 'here are some more contents again do you ')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2
    
    
    
    
