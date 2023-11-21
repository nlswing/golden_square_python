from lib.track import Track

'''
When a new instance of Track is made,
It's properties are returned.
'''

def test_properties_of_instance_returned():
    track = Track('Yellow', 'Coldplay')
    assert track.title == 'Yellow'
    assert track.artist == 'Coldplay'
    
'''
When a keyword matches the artist,
True is returned.
'''

def test_keyword_match_artist_returns_true():
    track_1 = Track('Yellow', 'Coldplay')
    assert track_1.matches('Coldplay') == True
    
'''
When a keyword matches the track title,
True is returned.
'''

def test_keyword_match_title_returns_true():
    track_1 = Track('Yellow', 'Coldplay')
    assert track_1.matches('Yellow') == True
    
'''
When a keyword does not match the track or title,
False is returned.
'''

def test_keyword_does_not_match_title_returns_true():
    track_1 = Track('Yellow', 'Coldplay')
    assert track_1.matches('123') == False
    
'''
When a keyword matches a partial title,
Matches is True
'''
def test_partial_keyword_match_title_returns_true():
    track_1 = Track('Yellow', 'Coldplay')
    assert track_1.matches('Yel') == True