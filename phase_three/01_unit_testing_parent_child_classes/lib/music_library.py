class MusicLibrary:
    

    def __init__(self):
        self._list_of_tracks = []

    def add(self, track):
        self._list_of_tracks.append(track)

    def search(self, keyword):
        matches = []
        for track in self._list_of_tracks:
            if track.matches(keyword):
                matches.append(track)
        return matches
            
        