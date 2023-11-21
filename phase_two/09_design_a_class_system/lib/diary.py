class Diary():
    def __init__(self):
        self._diary_entries = []
        self._task_list = []
        self._contact_list = []

    def add_diary_entry(self, entry):
        self._diary_entries.append(entry)
        

    def list_diary_entries(self):
        
        return self._diary_entries

    def select_diary_entry(self, wpm, time):
        readable_entries = []
        words_reader_can_read = wpm * time
        for entry in self._diary_entries:
            if entry.word_counter() <= words_reader_can_read:
                readable_entries.append(entry)
        return readable_entries
      

    def add_tasks(self):
        for entry in self._diary_entries:
            if entry.name == '#TODO':
                self._task_list.append(entry.contents)
                

    def list_tasks(self):
        return self._task_list

              
            
    def list_contacts(self):
        for entry in self._diary_entries:
            self._contact_list.append(entry.number_grabber())
            
        return self._contact_list
                    