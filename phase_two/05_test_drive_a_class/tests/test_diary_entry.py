from lib.diary_entry import *

'''
Returns a title and contents.
'''

def test_returns_an_empty_string():
    diary_entry = DiaryEntry("Title", "Contents")
    result = diary_entry.format()
    assert result == "Title: Contents"
    
'''
Returns the amount of words in a contents, if contents is a single word.
'''

def test_count_a_single_words_in_contents():
    diary_entry = DiaryEntry("Title", "Contents")
    result = diary_entry.count_words()
    assert result == 1
    
'''
Returns the amount of words in a contents, if contents is a many words.
'''

def test_amount_of_words_in_contents():
    diary_entry = DiaryEntry("Title", "Contents " * 100)
    result = diary_entry.count_words()
    assert result == 100
    
'''
Returns an estimated reading time of 1, given contents = 100 words and user reads at 100 wpm
'''

def test_reading_time_for_100_words_and_100_wpm():
    diary_entry = DiaryEntry("Title", "Contents " * 100)
    result = diary_entry.reading_time(100)
    assert result == 1
    
'''
Returns an estimated reading time of 240, given contents = 55000 words and user reads at 230 wpm
'''

def test_reading_time_for_50000_words_and_230_wpm():
    diary_entry = DiaryEntry("Title", "Contents " * 55000)
    result = diary_entry.reading_time(230)
    assert result == 240
    
'''
Returns 4 words if a reader reads at 1 wpm and has 4 minutes.
'''

def test_reader_has_4_mins_and_reads_1wpm():
    diary_entry = DiaryEntry("Title", "This is a selection from a text with ten words.")
    result = diary_entry.reading_chunk(1, 4)
    assert result == "This is a selection"
    
'''
Returns the next contents if some contents already read.
'''

def test_reader_has_the_next_chunk_of_contents():
    diary_entry = DiaryEntry("Title", "This is a selection from a text with ten words.")
    diary_entry.reading_chunk(1, 4)
    result = diary_entry.reading_chunk(1, 4)
    assert result == "from a text with"

    


    
    