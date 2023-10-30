from lib.tasks import *

def test_with_no_task_returns_empty_list():
    tracker = TaskTracker()
    result = tracker.list_incomplete()
    assert result == []

def test_with_single_task_returns_task_in_list():
    tracker = TaskTracker()
    tracker.add("Clean Kitchen")
    assert tracker.list_incomplete() == ["Clean Kitchen"]

def test_with_mulitple_tasks_return_list():
    tracker = TaskTracker()
    tracker.add("Clean Kitchen")
    tracker.add("Shopping")
    tracker.add("Wash dog")
    assert tracker.list_incomplete() == ["Clean Kitchen", "Shopping", "Wash dog"]

def test_if_task_completed_remove_from_list():
    tracker = TaskTracker()
    tracker.add("Clean kitchen") 
    tracker.add("shopping")
    tracker.add("Wash dog")
    tracker.mark_completed(1)
    assert tracker.list_incomplete() == ["Clean kitchen", "Wash dog"]

