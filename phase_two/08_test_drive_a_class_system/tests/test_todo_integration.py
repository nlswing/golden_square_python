from lib.todo import Todo
from lib.todo_list import TodoList

'''
When I add a todo
It is returned in a list of incomplete todos
'''

def test_add_a_todo_returns_that_todo_as_incomplete():
    todo_list = TodoList()
    task_1 = Todo('task 1')
    todo_list.add(task_1)
    assert todo_list.incomplete() == [task_1]
    
'''
When I add two todos
They are returned in a list of incomplete todos
'''

def test_add_two_todos_returns_those_todos_as_incomplete():
    todo_list = TodoList()
    task_1 = Todo('task 1')
    task_2 = Todo('task 2')
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_1, task_2]

'''
When I complete a task
It is added to a list of completed tasks.
'''

def test_when_task_completed_it_is_added_to_completed_task_list():
    todo_list = TodoList()
    task_1 = Todo('task 1')
    todo_list.add(task_1)
    task_1.mark_complete()
    assert todo_list.complete() == [task_1]
    
'''
When I complete multiple tasks
They are added to a list of completed tasks.
'''

def test_when_multiple_tasks_completed_they_are_added_to_completed_task_list():
    todo_list = TodoList()
    task_1 = Todo('task 1')
    task_2 = Todo('task 2')
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert todo_list.complete() == [task_1, task_2]
    
'''
When I call the #give_up method on a todo_list,
All tasks are moved to complete.
'''

def test_when_give_up_method_is_called_all_tasks_move_to_complete():
    todo_list = TodoList()
    task_1 = Todo('task 1')
    task_2 = Todo('task 2')
    task_3 = Todo('task 3')
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.give_up()
    assert todo_list.complete() ==  [task_1, task_2, task_3]
    
    

    

