"""
Unit tests for the mark_complete functionality.
Following TDD: Write tests first, implement code after.
"""

from typing import List

import pytest
from todo_list import TodoList


def test_mark_complete_by_index() -> None:
    """Test that marking a task as complete by index works correctly."""
    todo_list = TodoList()
    task = "Buy groceries"
    todo_list.add_task(task)

    # Mark the task as complete by index
    result = todo_list.mark_complete(0)

    # Verify the task was marked as complete and the method returns True
    assert result is True
    # We'll need to add a way to check completion status, but for now the method just marks it


def test_mark_complete_by_name() -> None:
    """Test that marking a task as complete by name works correctly."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Mark a task as complete by name
    result = todo_list.mark_complete("Walk the dog")

    # Verify the task was marked as complete and method returns True
    assert result is True


def test_mark_complete_returns_completion_status() -> None:
    """Test that mark_complete returns the completion status of the task."""
    todo_list = TodoList()
    task = "Buy groceries"
    todo_list.add_task(task)

    # First, mark the task as complete by index
    result1 = todo_list.mark_complete(0)
    assert result1 is True
    
    # Try marking it again - should still return True
    result2 = todo_list.mark_complete(0)
    assert result2 is True


def test_mark_complete_by_index_out_of_range() -> None:
    """Test that marking a task as complete by index that's out of range raises an IndexError."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # Try to mark task at index that doesn't exist
    with pytest.raises(IndexError):
        todo_list.mark_complete(5)


def test_mark_complete_by_name_not_found() -> None:
    """Test that marking a task as complete by name that doesn't exist raises a ValueError."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # Try to mark task that doesn't exist
    with pytest.raises(ValueError):
        todo_list.mark_complete("Non-existent task")


def test_mark_complete_on_empty_list_by_index() -> None:
    """Test that marking a task as complete from an empty list by index raises an IndexError."""
    todo_list = TodoList()

    # Try to mark task from empty list
    with pytest.raises(IndexError):
        todo_list.mark_complete(0)


def test_mark_complete_on_empty_list_by_name() -> None:
    """Test that marking a task as complete from an empty list by name raises a ValueError."""
    todo_list = TodoList()

    # Try to mark task from empty list
    with pytest.raises(ValueError):
        todo_list.mark_complete("Any task")


def test_view_completed_tasks() -> None:
    """Test that there's a way to view completed tasks specifically."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Mark some tasks as complete
    todo_list.mark_complete("Walk the dog")
    todo_list.mark_complete(0)  # "Buy groceries"

    # With our planned implementation, we'll add view_completed_tasks method
    # This test will pass once we implement the view_completed_tasks functionality
    completed_tasks = todo_list.view_completed_tasks()
    assert "Walk the dog" in completed_tasks
    assert "Buy groceries" in completed_tasks
    assert "Clean the house" not in completed_tasks


def test_view_pending_tasks() -> None:
    """Test that there's a way to view pending (not completed) tasks."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Mark some tasks as complete
    todo_list.mark_complete("Walk the dog")

    # With our planned implementation, we'll add view_pending_tasks method
    pending_tasks = todo_list.view_pending_tasks()
    assert "Walk the dog" not in pending_tasks
    assert "Buy groceries" in pending_tasks
    assert "Clean the house" in pending_tasks


def test_view_tasks_shows_all_with_status() -> None:
    """Test that view_tasks can show all tasks with their completion status."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Mark one task as complete
    todo_list.mark_complete("Walk the dog")

    # Check that view_tasks returns tasks in an appropriate format
    all_tasks = todo_list.view_tasks_with_status()
    # This should return tasks with completion status
    task_dict = {task['task']: task['completed'] for task in all_tasks}
    assert task_dict["Walk the dog"] is True
    assert task_dict["Buy groceries"] is False
    assert task_dict["Clean the house"] is False