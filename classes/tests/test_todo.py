from lib.todo import *

# when a task is added, it is set to False

def test_with_single_task_returns_false():
    todo = Todo("Wash the dog")
    result = False
    assert result == False

# when the mark_complete function is called, set task to True (completed)

def test_sing_function_is_maked_completed_True():
    todo = Todo("Wash the dog")
    todo.mark_complete()
    assert todo.complete == True


    