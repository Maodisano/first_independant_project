from lib.todo_list import *

# when no task is added, returns an empty list

def test_with_no_task_returns_empty_list():
    todo_list = TodoList()
    result = todo_list.incomplete()
    assert result == []

# 

