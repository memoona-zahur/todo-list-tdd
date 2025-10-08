"""
Unit tests for the delete_task functionality.
Following TDD: Write tests first, implement code after.
"""

from typing import List

import pytest
from todo_list import TodoList


def test_delete_task_by_index_single_task() -> None:
    """Test that deleting a task by index works for a single task."""
    todo_list = TodoList()
    task = "Buy groceries"
    todo_list.add_task(task)

    # Delete the task by index (0)
    deleted_task = todo_list.delete_task(0)

    # Verify the task was deleted and returned
    assert deleted_task == task
    assert len(todo_list.tasks) == 0


def test_delete_task_by_index_multiple_tasks() -> None:
    """Test that deleting a task by index works with multiple tasks."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Delete the second task (index 1)
    deleted_task = todo_list.delete_task(1)

    # Verify the correct task was deleted and returned
    assert deleted_task == "Walk the dog"
    assert len(todo_list.tasks) == 2
    assert "Walk the dog" not in todo_list.tasks
    assert "Buy groceries" in todo_list.tasks
    assert "Clean the house" in todo_list.tasks


def test_delete_task_by_index_first_task() -> None:
    """Test that deleting the first task by index works."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Delete the first task (index 0)
    deleted_task = todo_list.delete_task(0)

    # Verify the correct task was deleted
    assert deleted_task == "Buy groceries"
    assert len(todo_list.tasks) == 2
    assert "Buy groceries" not in todo_list.tasks
    remaining_tasks = todo_list.view_tasks()
    assert remaining_tasks == ["Walk the dog", "Clean the house"]


def test_delete_task_by_index_last_task() -> None:
    """Test that deleting the last task by index works."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Delete the last task (index 2)
    deleted_task = todo_list.delete_task(2)

    # Verify the correct task was deleted
    assert deleted_task == "Clean the house"
    assert len(todo_list.tasks) == 2
    assert "Clean the house" not in todo_list.tasks
    remaining_tasks = todo_list.view_tasks()
    assert remaining_tasks == ["Buy groceries", "Walk the dog"]


def test_delete_task_by_name_existing_task() -> None:
    """Test that deleting a task by name works for an existing task."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Delete a task by name
    deleted_task = todo_list.delete_task("Walk the dog")

    # Verify the correct task was deleted and returned
    assert deleted_task == "Walk the dog"
    assert len(todo_list.tasks) == 2
    assert "Walk the dog" not in todo_list.tasks
    assert "Buy groceries" in todo_list.tasks
    assert "Clean the house" in todo_list.tasks


def test_delete_task_by_name_duplicate_tasks() -> None:
    """Test that deleting a task by name works when there are duplicates."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Buy groceries"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Delete a task by name (should remove the first occurrence)
    deleted_task = todo_list.delete_task("Buy groceries")

    # Verify the first occurrence was deleted
    assert deleted_task == "Buy groceries"
    assert len(todo_list.tasks) == 2
    # One "Buy groceries" should remain
    assert todo_list.tasks.count("Buy groceries") == 1
    assert "Walk the dog" in todo_list.tasks


def test_delete_task_by_index_out_of_range() -> None:
    """Test that deleting a task by index that's out of range raises an IndexError."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # Try to delete task at index that doesn't exist
    with pytest.raises(IndexError):
        todo_list.delete_task(5)


def test_delete_task_by_name_not_found() -> None:
    """Test that deleting a task by name that doesn't exist raises a ValueError."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # Try to delete task that doesn't exist
    with pytest.raises(ValueError):
        todo_list.delete_task("Non-existent task")


def test_delete_from_empty_list_by_index() -> None:
    """Test that deleting a task from an empty list by index raises an IndexError."""
    todo_list = TodoList()

    # Try to delete task from empty list
    with pytest.raises(IndexError):
        todo_list.delete_task(0)


def test_delete_from_empty_list_by_name() -> None:
    """Test that deleting a task from an empty list by name raises a ValueError."""
    todo_list = TodoList()

    # Try to delete task from empty list
    with pytest.raises(ValueError):
        todo_list.delete_task("Any task")