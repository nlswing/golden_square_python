from lib.todo_list import TodoList

'''
Initially, the complete task list is empty.
''' 

def test_todo_list_is_empty_on_initialising():
    todo_list = TodoList()
    assert todo_list._todos == []
    
'''
Initially, the incomplete task list is empty.
''' 

def test_completed_list_is_empty_on_initialising():
    todo_list = TodoList()
    assert todo_list.complete() == []