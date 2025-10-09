"""
Unit tests for the view_tasks functionality.
Following TDD: Write tests first, implement code after.
"""

from typing import List

import pytest
from todo.todo_list import TodoList


def test_view_tasks_empty_list() -> None:
    """Test that viewing tasks returns an empty list when no tasks exist."""
    todo_list = TodoList()

    tasks = todo_list.view_tasks()

    assert tasks == []
    assert len(tasks) == 0


def test_view_tasks_single_task() -> None:
    """Test that viewing tasks returns a list with one task."""
    todo_list = TodoList()
    task = "Buy groceries"
    todo_list.add_task(task)

    tasks = todo_list.view_tasks()

    assert isinstance(tasks, List)
    assert len(tasks) == 1
    assert task in tasks


def test_view_tasks_multiple_tasks() -> None:
    """Test that viewing tasks returns a list with multiple tasks."""
    todo_list = TodoList()
    tasks_to_add = ["Buy groceries", "Walk the dog", "Clean the house"]

    for task in tasks_to_add:
        todo_list.add_task(task)

    tasks = todo_list.view_tasks()

    assert isinstance(tasks, List)
    assert len(tasks) == 3
    for task in tasks_to_add:
        assert task in tasks


def test_view_tasks_returns_copy_not_reference() -> None:
    """Test that viewing tasks returns a copy, not a reference to internal list."""
    todo_list = TodoList()
    original_task = "Original task"
    todo_list.add_task(original_task)

    tasks = todo_list.view_tasks()
    tasks.append("Modified task")  # Modify the returned list

    # Internal list should not be affected
    internal_tasks = todo_list.view_tasks()
    assert len(internal_tasks) == 1
    assert "Modified task" not in internal_tasks


def test_view_tasks_after_removing_task() -> None:
    """Test that viewing tasks reflects changes after adding/removing tasks."""
    todo_list = TodoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")

    tasks_before = todo_list.view_tasks()
    assert len(tasks_before) == 2

    # Add another task
    todo_list.add_task("Task 3")
    tasks_after = todo_list.view_tasks()

    assert len(tasks_after) == 3
    assert "Task 3" in tasks_after
