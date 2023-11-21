from lib.music_library import MusicLibrary
from lib.track import Track

'''
When I add two tracks,
They are returned in a list.
'''

def test_tracks_are_added_to_the_list():
    music_library = MusicLibrary()
    track_1 = Track('Creep', 'Radiohead')
    track_2 = Track('Yellow', 'Coldplay')
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library._list_of_tracks == [track_1, track_2]
    
'''
When I search for a track by a keyword,
The track(s) is/are returned that link to keyword
'''

def test_tracks_relating_to_keyword_are_returned():
    music_library = MusicLibrary()
    track_1 = Track('Creep', 'Radiohead')
    track_2 = Track('Yellow', 'Coldplay')
    track_3 = Track('Wonderwall', 'Oasis')
    track_4 = Track('Sparks', 'Coldplay')
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    music_library.add(track_4)
    assert music_library.search('Coldplay') == [track_2, track_4]