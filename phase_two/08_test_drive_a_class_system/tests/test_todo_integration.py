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

    

