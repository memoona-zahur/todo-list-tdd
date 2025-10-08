"""
Unit tests for the Todo List functionality.
Following TDD: Write tests first, implement code after.
"""

import pytest
from todo_list import TodoList


def test_add_task() -> None:
    """Test that adding a task works correctly."""
    todo_list = TodoList()
    initial_task_count = len(todo_list.tasks)

    # Add a task
    task = "Buy groceries"
    todo_list.add_task(task)

    # Verify the task was added
    assert len(todo_list.tasks) == initial_task_count + 1
    assert task in todo_list.tasks


def test_add_multiple_tasks() -> None:
    """Test that adding multiple tasks works correctly."""
    todo_list = TodoList()

    # Add multiple tasks
    tasks = ["Buy groceries", "Walk the dog", "Clean the house"]
    for task in tasks:
        todo_list.add_task(task)

    # Verify all tasks were added
    assert len(todo_list.tasks) == 3
    for task in tasks:
        assert task in todo_list.tasks


def test_add_empty_task() -> None:
    """Test that adding an empty task works."""
    todo_list = TodoList()

    # Add an empty task
    todo_list.add_task("")

    # Verify the empty task was added
    assert len(todo_list.tasks) == 1
    assert "" in todo_list.tasks


def test_add_task_with_special_characters() -> None:
    """Test that adding tasks with special characters works."""
    todo_list = TodoList()

    # Add a task with special characters
    special_task = "Buy groceries & cook dinner @ home #1"
    todo_list.add_task(special_task)

    # Verify the task was added
    assert special_task in todo_list.tasks
