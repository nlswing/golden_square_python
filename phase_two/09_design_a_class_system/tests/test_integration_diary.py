from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given two diary entries are added,
We see those tracks entries in the diary_entries list.
"""

def test_diary_entries_added_to_list():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Here is my first diary entry.")
    entry_2 = DiaryEntry("Entry 2", "Here is my second diary entry, isn't that nice?")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.list_diary_entries() == [entry_1, entry_2]
    
'''
Given the user sepcifies their reading speed and time,
The entries that can be read with the given parameters are returned. 
'''

def test_most_appropriate_entry_is_returned_based_on_user_reading_speed_time():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Here is my first diary entry.")
    entry_2 = DiaryEntry("Entry 2", "Here is my second diary entry, isn't that nice?")
    entry_3 = DiaryEntry("Entry 3", "Here's another entry and this is going to be a bit longer than the other entries that I have entered.")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    diary.add_diary_entry(entry_3)
    assert diary.select_diary_entry(3, 2) == [entry_1]
    
'''
Given two tasks are added to the diary,
We see those task entries in the task_list.
'''
def test_dairy_entries_with_a_todo_are_added_to_task_list():
    diary = Diary()
    entry_1 = DiaryEntry("#TODO", "Walk the dog")
    entry_2 = DiaryEntry("Entry 1", "Here a diary entry")
    entry_3 = DiaryEntry("#TODO", "Wash the car")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    diary.add_diary_entry(entry_3)
    diary.add_tasks()
    assert diary.list_tasks() == ["Walk the dog", "Wash the car"]
    
'''
Given two contacts are added to the diary,
We see those task entries in the contacts_list.
'''

def test_contacts_are_pulled_from_diary_entries_and_added_to_list():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Dave's number is 071234567890")
    entry_2 = DiaryEntry("Entry 2", "Mary's number is 071234567891")
    diary.add_diary_entry(entry_1)
    diary.add_diary_entry(entry_2)
    assert diary.list_contacts() == ['071234567890', '071234567891']
    