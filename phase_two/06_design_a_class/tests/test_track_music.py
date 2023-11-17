import pytest
from lib.track_music import *

def test_empty_list_on_init():
    music_tracker = MusicTracker()
    result = music_tracker.list_tracks()
    assert result == []
    
def test_addded_track_in_list():
    music_tracker = MusicTracker()
    music_tracker.add_track('creep')
    result = music_tracker.list_tracks()
    assert result == ['creep']
    
def test_multiple_added_tracks_appear_in_list():
    music_tracker = MusicTracker()
    music_tracker.add_track('creep')
    music_tracker.add_track('something')
    result = music_tracker.list_tracks()
    assert result == ['creep', 'something']
    
def test_exception_if_track_already_in_list():
    music_tracker = MusicTracker()
    
    with pytest.raises(Exception) as e:
        music_tracker.add_track('creep')
        music_tracker.add_track('creep')
        
    error_message = str(e.value)
    assert error_message == "Track has already been added."