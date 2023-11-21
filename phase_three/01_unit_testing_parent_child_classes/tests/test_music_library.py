from unittest.mock import Mock
from lib.music_library import MusicLibrary

'''
On initialising,
List of tracks is empty.
'''

def test_initialise_with_empty_list_of_tracks():
    music_library = MusicLibrary()
    assert music_library._list_of_tracks == []
    
'''
On matching two tracks with a keyword,
Those tracks are returned in a list.
'''

def test_tracks_with_matching_keyword_are_added_to_list():
    music_library = MusicLibrary()
    track_1_mock = Mock()
    track_1_mock.matches.return_value = True
    music_library.add(track_1_mock)
    track_2_mock = Mock()
    track_2_mock.matches.return_value = False
    music_library.add(track_2_mock)
    assert music_library.search('Yellow') == [track_1_mock]
    
'''
When I add some tracks,
They are added to the track list.
'''

def test_tracks_added_to_list():
    music_library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library._list_of_tracks ==[track_1, track_2, track_3]
