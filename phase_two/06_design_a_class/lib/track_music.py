class MusicTracker():
    def __init__(self):
        self.list_of_tracks = []
        
    def add_track(self, track_name):
        if track_name in self.list_of_tracks:
            raise Exception("Track has already been added.")
        self.list_of_tracks.append(track_name)
    
    def list_tracks(self):
        return self.list_of_tracks