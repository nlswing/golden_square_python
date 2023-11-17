import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        pass

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())
        

    def reading_time(self, wpm):
        est_reading_time = self.count_words() / wpm
        return math.ceil(est_reading_time)
        

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        contents_already_read = []
        words = self.contents.split()
        amount_user_can_read_in_given_time = wpm * minutes
        already_read = len(contents_already_read)
        words_reader_can_read = words[already_read:amount_user_can_read_in_given_time]
        contents_already_read.append((' '.join(words_reader_can_read)))
        return (''.join(contents_already_read))
        