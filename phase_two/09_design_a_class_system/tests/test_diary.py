from lib.diary import Diary

'''
On intialising,
Diary entries are empty.
'''

def test_intialise_empty_diary_entries():
    diary = Diary()
    assert diary._diary_entries == []
    
'''
On intialising,
Task list is empty.
'''

def test_intialise_empty_task_list():
    diary = Diary()
    assert diary._task_list == []
    
'''
On intialising,
Contact list is empty.
'''

def test_intialise_empty_contact_list():
    diary = Diary()
    assert diary._contact_list == []