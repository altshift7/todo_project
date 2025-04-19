# test_task_manager.py

from task_manager import TaskManager

def test_add_and_get_tasks():
    tm = TaskManager()
    tm.add_task("Do homework")
    assert tm.get_tasks() == ["Do homework"]

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Buy milk")
    tm.complete_task(0)
    assert tm.get_tasks() == []
    assert tm.get_completed_tasks() == ["Buy milk"]

def test_complete_invalid_task():
    tm = TaskManager()
    tm.add_task("Task A")
    tm.complete_task(5)  # Invalid index
    assert tm.get_tasks() == ["Task A"]
    assert tm.get_completed_tasks() == []
