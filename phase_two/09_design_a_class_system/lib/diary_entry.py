class DiaryEntry:
    # User-facing properties:
    #   name: string
    #   contents: string
    pass
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def word_counter(self):
       return len(self.contents.split())
   
    def number_grabber(self):
        split_content = self.contents.split()
        for x in split_content:
            if '0' in x:
                return x
           
    