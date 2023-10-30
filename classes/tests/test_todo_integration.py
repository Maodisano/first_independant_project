from lib.todo_list import *
from lib.todo import *

# when a task is added, returns task as incomplete 

def test_with_single_task_return_incompleted():
    todo_list = TodoList()
    todo1 = Todo("Wash the dog")
    todo_list.add(todo1)
    assert todo_list.incomplete() == [todo1]




def test_with_single_task_return_in_complete():
    todo_list = TodoList()
    todo1 = Todo("Wash the dog")
    todo_list.add(todo1)
    todo1.mark_complete()
    assert todo_list.complete() == [todo1]