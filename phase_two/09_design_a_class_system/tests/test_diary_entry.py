from lib.diary_entry import DiaryEntry

''' 
On initialising,
The task name and contents properties are returned.
'''

def test_diary_entry_properties_on_init():
    diary_entry = DiaryEntry('entry 1', 'Today I lost my dog.')
    assert diary_entry.name == 'entry 1'
    assert diary_entry.contents == 'Today I lost my dog.'
    
'''
On calling #word_counter method,
The length of the entry is returned as an integer.
'''

def test_word_counter_on_entry():
    diary_entry = DiaryEntry('entry 1', 'Today I lost my dog.')
    assert diary_entry.word_counter() == 5
    
'''
On calling #number_grabber method,
The number is extracted from the contents.
'''

def test_number_grabber_extracts_numbers_from_entry():
    entry_1 = DiaryEntry("Entry 1", "Dave's number is 071234567890")
    assert entry_1.number_grabber() == '071234567890'
     