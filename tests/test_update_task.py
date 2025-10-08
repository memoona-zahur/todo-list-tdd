"""
Unit tests for the update_task functionality.
Following TDD: Write tests first, implement code after.
"""

from typing import List

import pytest
from todo_list import TodoList


def test_update_task_by_index() -> None:
    """Test that updating a task by index works correctly."""
    todo_list = TodoList()
    initial_task = "Buy groceries"
    todo_list.add_task(initial_task)

    # Update the task by index
    old_task = todo_list.update_task(0, "Buy food")

    # Verify the task was updated and old task was returned
    assert old_task == initial_task
    assert len(todo_list.tasks) == 1
    assert "Buy food" in todo_list.tasks
    assert initial_task not in todo_list.tasks
    assert todo_list.tasks[0] == "Buy food"


def test_update_task_by_name() -> None:
    """Test that updating a task by name works correctly."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Update a task by name
    old_task = todo_list.update_task("Walk the dog", "Take the dog for a walk")

    # Verify the task was updated and old task was returned
    assert old_task == "Walk the dog"
    assert len(todo_list.tasks) == 3
    assert "Take the dog for a walk" in todo_list.tasks
    assert "Walk the dog" not in todo_list.tasks
    # Other tasks should remain unchanged
    assert "Buy groceries" in todo_list.tasks
    assert "Clean the house" in todo_list.tasks


def test_update_task_multiple_occurrences_by_name() -> None:
    """Test that updating a task by name updates the first occurrence."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Buy groceries"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Update the first occurrence of "Buy groceries"
    old_task = todo_list.update_task("Buy groceries", "Buy food items")

    # Verify only the first occurrence was updated
    assert old_task == "Buy groceries"
    assert len(todo_list.tasks) == 3
    assert todo_list.tasks.count("Buy groceries") == 1  # One remaining
    assert todo_list.tasks.count("Buy food items") == 1  # One updated
    assert "Buy food items" in todo_list.tasks
    assert todo_list.tasks[0] == "Buy food items"  # First occurrence updated


def test_update_task_by_index_multiple_tasks() -> None:
    """Test that updating a task by index works with multiple tasks."""
    todo_list = TodoList()
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    
    for task in tasks:
        todo_list.add_task(task)

    # Update the second task (index 1)
    old_task = todo_list.update_task(1, "Take the dog for a walk")

    # Verify the correct task was updated
    assert old_task == "Walk the dog"
    assert len(todo_list.tasks) == 3
    assert "Take the dog for a walk" in todo_list.tasks
    assert "Walk the dog" not in todo_list.tasks
    assert todo_list.tasks[1] == "Take the dog for a walk"
    # Other tasks should remain unchanged
    assert todo_list.tasks[0] == "Buy groceries"
    assert todo_list.tasks[2] == "Clean the house"


def test_update_task_by_index_out_of_range() -> None:
    """Test that updating a task by index that's out of range raises an IndexError."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # Try to update task at index that doesn't exist
    with pytest.raises(IndexError):
        todo_list.update_task(5, "New task")


def test_update_task_by_name_not_found() -> None:
    """Test that updating a task by name that doesn't exist raises a ValueError."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")

    # Try to update task that doesn't exist
    with pytest.raises(ValueError):
        todo_list.update_task("Non-existent task", "New task")


def test_update_task_on_empty_list_by_index() -> None:
    """Test that updating a task from an empty list by index raises an IndexError."""
    todo_list = TodoList()

    # Try to update task from empty list
    with pytest.raises(IndexError):
        todo_list.update_task(0, "Any task")


def test_update_task_on_empty_list_by_name() -> None:
    """Test that updating a task from an empty list by name raises a ValueError."""
    todo_list = TodoList()

    # Try to update task from empty list
    with pytest.raises(ValueError):
        todo_list.update_task("Any task", "New task")


def test_update_task_to_same_value() -> None:
    """Test that updating a task to the same value works correctly."""
    todo_list = TodoList()
    task = "Buy groceries"
    todo_list.add_task(task)

    # Update the task to the same value
    old_task = todo_list.update_task(0, "Buy groceries")

    # Verify the task remains the same
    assert old_task == "Buy groceries"
    assert len(todo_list.tasks) == 1
    assert task in todo_list.tasks
    assert todo_list.tasks[0] == "Buy groceries"


def test_update_task_with_special_characters() -> None:
    """Test that updating a task with special characters works correctly."""
    todo_list = TodoList()
    original_task = "Buy groceries & cook dinner @ home #1"
    new_task = "Cook dinner & buy ingredients $20 *special*"
    todo_list.add_task(original_task)

    # Update the task with special characters
    old_task = todo_list.update_task(0, new_task)

    # Verify the task was updated correctly
    assert old_task == original_task
    assert new_task in todo_list.tasks
    assert original_task not in todo_list.tasks
    assert todo_list.tasks[0] == new_task