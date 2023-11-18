from math import ceil

class Diary:
    def __init__(self):
        self._diary_entires = []
        

    def add(self, entry):
        self._diary_entires.append(entry)
        pass

    def all(self):
        return self._diary_entires

    def count_words(self):
        total_words = 0 
        for entry in self._diary_entires:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        if self._diary_entires == []:
            raise Exception("No entries added yet.")
        words = self.count_words()
        return ceil(words / wpm)
      
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._diary_entires == []:
            raise Exception("No entries added yet.")
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self._diary_entires:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable
       
                




