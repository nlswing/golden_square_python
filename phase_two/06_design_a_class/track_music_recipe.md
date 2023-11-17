## Keep Track of Listening Design Recipe


1. Describe the Problem
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class MusicTracker:
    

    def __init__(self):
        # Empty list initialised
        self.list_of_tracks = []
        pass # No code here yet

    def add_track(self, track_name):
        # Parameters:
        #   track_name: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Throws exception if track is already in list.
        pass # No code here yet

    def list_music(self):
        # Returns:
        #   A list of tracks that have been listened to.
        # Side-effects:
        #   None
        pass # No code here yet
3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
On initialisation
#empty list is returned
"""
music_tracker = MusicTracker()
music_tracker.list_music() # => []


"""
On adding a track, a track appears in the list.
#track appears in list
"""
music_tracker = MusicTracker()
music_tracker.add_track('creep')
music_tracker.list_music() # => ['creep']

"""
On adding multiple tracks, a tracks appear in the list.
#tracks appear in list
"""
music_tracker = MusicTracker()
music_tracker.add_track('creep')
music_tracker.add_track('something')
music_tracker.list_music() # => ['creep', 'something']

"""
If track already exists in list and the same track is added.
#Throws exception.
"""
music_tracker = MusicTracker()
music_tracker.add_track('creep')
music_tracker.add_track('creep')
music_tracker.list_music() # => Err 'Track already in list'.

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.