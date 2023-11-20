from lib.todo import Todo

'''
When I initialise the class with a task,
that task is returned in the dictionary
and is set to false.
'''

def test_initialising_class_returns_task_in_dictionary_set_to_false():
    todo = Todo('task 1')
    assert todo.task_list == { 'task': 'task 1', 'complete': False }
    
'''
When #mark_complete method is called on a task,
It's complete property is changed to True.
'''

def test_mark_complete_changes_task_to_true():
    todo = Todo('task 1')
    todo.mark_complete()
    assert todo.task_list == { 'task': 'task 1', 'complete': True }