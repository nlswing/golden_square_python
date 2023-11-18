from lib.diary_entry import DiaryEntry

'''
When I initialise with a title and contents
I can get that title and contents back 
'''

def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry('My title', 'My contents')
    assert diary_entry.title == 'My title'
    assert diary_entry.contents == 'My contents'


'''
Returns the number representing the number of words in the contents of the entry.
'''

def test_count_words_in_entry():
    diary_entry = DiaryEntry('my title 1', 'my contents here')
    assert diary_entry.count_words() == 3

'''
When I initialise with a five-word contents
the #reading_time with a wpm of 2 should return 3
'''

def test_reading_time():
    diary_entry = DiaryEntry('My Title', 'this is some content here')
    assert diary_entry.reading_time(2) == 3
    
'''
When I initialise with a five-word contents
Then, at first, #reading_chunk should return the first chunk
readable in the time
'''

def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry('My Title', 'this is some content here')
    assert diary_entry.reading_chunk(2, 1) == 'this is'
    
    
'''
When I initialise with a five-word contents
Then, on the second call, #reading_chunk should return the second chunk
readable in the time
'''
def test_readable_chunk_second_chunk():
    diary_entry = DiaryEntry('My Title', 'this is some content here')
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == 'some content'
    
    '''
    When I initialise with a five-word contents
    Then, on the third call, #reading_chunk should return the final, partial chunk
    '''
    
def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry('My Title', 'this is some content here')
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == 'here'
    
    
'''
When I initialise with a five-word contents
Then on the fourth call, #reading chunk should start again from beginning
'''

def test_readable_chunk_fourth_chunk():
    diary_entry = DiaryEntry('My Title', 'this is some content here')
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == "this is" 
    
'''
When I initialise with a six-word contents
Then on the fourth call, #reading chunk should start again from beginning
'''

def test_readable_chunk_fourth_chunk_with_exact_chunks():
    diary_entry = DiaryEntry('My Title', 'this is some content here ok')
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == "this is" 
    
    
    
    