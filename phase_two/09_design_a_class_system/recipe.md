Filofax Multi-Class Planned Design Recipe

1. Describe the Problem
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com


   ┌────────────────────────────┐   ┌────────────────────────┐
   │ class Diary()              │   │ class Task()           │
   │ - add diary entry          │   │  - init(name)          │
   │ - list diary entries(name) │   │  #TODO                 │
   │ - select diary entry(wmp, time)│                        │
   │ - add task(task)           │   │                        │
   │ - list tasks()             ├──►│                        │
   │ - number_grabber()         │   │                        │
   │ - list contacts()          │   │                        │
   └─────────────┬──────────────┤   └────────────────────────┘
                 │              │
   ┌─────────────▼──────────────┤     
   │ class DiaryEntry           │     
   │ - init(name, contents)     │      
   │ - format()                 │      
   │ - word_count()             |
   │                            │      
   │                            │      
   │                            │      
   │                            │      
   └────────────────────────────┘      

Also design the interface of each class in more detail.

class Diary:
    #   User-facing properties:
    #   diary entries: list of instances of DiaryEntry
    #   tasks: list of instances of Task
    #   contacts: list of instances of Contacts

    def __init__(self):
        self._diary_entries = []
        self.task_list = []
        self.contact_list = []

    def add_diary_entry(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the diary_entries property of the self object
        pass # No code here yet

    def list_diary_entries(self):
        # Parameters:
        #  none
        # Returns:
        #   A list of the DiaryEntry instances 
        pass # No code here yet

    def select_diary_entry(self, wpm, time):
        # Parameters:
        #   wpm: integer the words per minute the user can read
        #   time: the time the user has to read
        # Returns:
        #   The instances of DiaryEntries that are appropriate based on the wpm, and amount of time the user has.
        

    def add_tasks():
        # Parameters:
        #   none
        # Side-effects:
        #   Identifies task that are in DiaryEntry instances and adds to the task_list property of the self object.
        pass # No code here yet

    def list_tasks(self):
        # Parameters:
        #  none
        # Returns:
        #   A list of the tasks that have been added to the task_list property
        pass # No code here yet

     def number_grabber(self):
        # Parameters:
        #   none
        # Side-effects:
        #   Identifies the nnumbers in DiaryEntry instances and adds the contact to the contact_list property of the self object
        pass # No code here yet

    def list_contacts(self):
        # Parameters:
        #  none
        # Returns:
        #   A list of the Contacts instances 
        pass # No code here yet

class DiaryEntry:
    # User-facing properties:
    #   name: string
    #   contents: string

    def __init__(self, name, contents):
        # Parameters:
        #   name: string
        #   contents: string
        # Side-effects:
        #   Sets the name and contents properties
        pass # No code here yet

    def word_counter()
         # Parameters:
        #   none
        # Returns the amount of words in the content of the #entry.
        # Side-effects:
        #   None
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "NAME: CONTENTS"
        pass # No code here yet

<!-- class Task():
    # User-facing properties:
    #   task: string

    def __init__(self, task):
        # Parameters:
        #   task: string
        # Side-effects:
        #   Sets the name a property
        pass # No code here yet

class Contacts():
    # User-facing properties:
    #  name: string
    #  number: string

    def __init__(self, name, number):
        # Parameters:
        #   name: string
        #   number: string
        # Side-effects:
        #   Sets the name and number properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "NAME: 01234567890"
        pass # No code here yet -->

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
Given two diary entries are added,
We see those tracks entries in the diary_entries list.
"""
diary = Diary()
entry_1 = DiaryEntry("Entry 1", "Here is my first diary entry.")
entry_2 = DiaryEntry("Entry 2", "Here is my second diary entry, isn't that nice?")
diary.add(entry_1)
diary.add(entry_2)
diary.list_diary_entries # => [entry_1, entry_2]

'''
Given the user sepcifies their reading speed and time,
The entries that can be read are returned. 
'''
diary = Diary()
entry_1 = DiaryEntry("Entry 1", "Here is my first diary entry.")
entry_2 = DiaryEntry("Entry 2", "Here is my second diary entry, isn't that nice?")
entry_3 = DiaryEntry("Entry 3", "Here's another entry and this is going to be a bit longer than the other entries that I have entered.)
diary.add_diary_entry(entry_1)
diary.add_diary_entry(entry_2)
diary.add_diary_entry(entry_3)
diary.select_diary_entry(3, 2) # => entry_1

'''
Given two tasks are added to the diary,
We see those task entries in the task_list.
'''
diary = Diary()
entry_1 = DiaryEntry("#TODO", "Walk the dog.")
entry_2 = DiaryEntry("Entry 1", "Here a diary entry")
entry_2 = DiaryEntry("#TODO", "Wash the car.")
diary.add_tasks()
diary.list_tasks # => ["Walk the dog.", "Wash the car."]

'''
Given two contacts are added to the diary,
We see those task entries in the contacts_list.
'''
diary = Diary()
entry_1 = DiaryEntry("Entry 1", "Dave's number is 071234567890")
entry_2 = DiaryEntry("Entry 2", "Mary's number is 071234567891")
diary.number_grabber()
diary.list_contacts # => [071234567890, 071234567891]



4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

Diary Unit Tests

"""
On initialising,
An empty diary entries list is returned.
"""

diary = Diary()
self._diary_entries # =>  []

"""
On initialising,
An empty task list is returned.
"""

diary = Diary()
self._task_list # =>  []

"""
On initialising,
An empty contacts list is returned.
"""

diary = Diary()
self._contact_list # =>  []

DiaryEntry Unit Tests

''' 
On initialising,
The task name and contents properties are returned.
'''

diary_entry = DiaryEntry('entry 1', 'Today I lost my dog.')
diary_entry.name # => 'entry 1'
diary_entry.contents # => 'Today I lost my dog.'

'''
On calling the #format method,
The name and contens are returned in a formatted way.
'''
diary_entry = DiaryEntry('entry 1', 'Today I lost my dog.')
diary_entry.format # => 'ENTRY NAME: entry 1 CONTENTS: 'Today I lost my dog.'




5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.