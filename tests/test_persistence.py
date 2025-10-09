"""
Unit tests for the persistence functionality (save_tasks and load_tasks).
Following TDD: Write tests first, implement code after.
"""

import json
import os
import tempfile
from typing import List, Dict, Any, Union

import pytest
from todo.todo_list import TodoList


def test_save_tasks_to_json_file() -> None:
    """Test that save_tasks creates a valid JSON file with tasks."""
    todo_list = TodoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Walk the dog")
    
    # Mark one task as complete
    todo_list.mark_complete("Walk the dog")
    
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_filename = temp_file.name
    
    try:
        # Import the function we're testing
        from todo.todo_list import save_tasks
        
        # Save tasks to the temporary file
        save_tasks(todo_list, temp_filename)
        
        # Verify the file exists
        assert os.path.exists(temp_filename)
        
        # Verify the file contains valid JSON
        with open(temp_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Verify the structure of the saved data
        assert isinstance(data, list)
        assert len(data) == 2
        
        # Verify the tasks have the correct structure
        expected_tasks = [
            {"task": "Buy groceries", "completed": False},
            {"task": "Walk the dog", "completed": True}
        ]
        
        # Check that the content matches expected
        for i, expected_task in enumerate(expected_tasks):
            assert data[i]["task"] == expected_task["task"]
            assert data[i]["completed"] == expected_task["completed"]
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_load_tasks_from_empty_file() -> None:
    """Test that load_tasks works with an empty JSON file (empty list)."""
    # Create a temporary file with empty list
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        json.dump([], temp_file)
        temp_filename = temp_file.name
    
    try:
        # Import the function we're testing
        from todo.todo_list import load_tasks
        
        todo_list = TodoList()
        
        # Load tasks from the temporary file
        load_tasks(todo_list, temp_filename)
        
        # Verify that the todo list is empty
        assert len(todo_list.tasks) == 0
        assert todo_list.tasks == []
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_load_tasks_from_json_file() -> None:
    """Test that load_tasks correctly loads tasks from a JSON file."""
    # Create test data
    test_tasks = [
        {"task": "Buy groceries", "completed": False},
        {"task": "Walk the dog", "completed": True},
        {"task": "Clean the house", "completed": False}
    ]
    
    # Create a temporary file with test data
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        json.dump(test_tasks, temp_file)
        temp_filename = temp_file.name
    
    try:
        # Import the function we're testing
        from todo.todo_list import load_tasks
        
        todo_list = TodoList()
        
        # Load tasks from the temporary file
        load_tasks(todo_list, temp_filename)
        
        # Verify that the correct number of tasks were loaded
        assert len(todo_list.tasks) == 3
        
        # Verify the tasks have the correct content and completion status
        assert todo_list.tasks[0]["task"] == "Buy groceries"
        assert todo_list.tasks[0]["completed"] is False
        
        assert todo_list.tasks[1]["task"] == "Walk the dog"
        assert todo_list.tasks[1]["completed"] is True
        
        assert todo_list.tasks[2]["task"] == "Clean the house"
        assert todo_list.tasks[2]["completed"] is False
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_save_and_load_cycle() -> None:
    """Test that saving and then loading preserves task data."""
    # Set up initial todo list
    original_todo_list = TodoList()
    original_todo_list.add_task("Task 1")
    original_todo_list.add_task("Task 2")
    original_todo_list.mark_complete("Task 1")  # Mark first task as complete
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_filename = temp_file.name
    
    try:
        # Import the functions we're testing
        from todo.todo_list import save_tasks, load_tasks
        
        # Save the original todo list
        save_tasks(original_todo_list, temp_filename)
        
        # Create a new todo list and load from file
        new_todo_list = TodoList()
        load_tasks(new_todo_list, temp_filename)
        
        # Verify that the new list matches the original
        assert len(new_todo_list.tasks) == len(original_todo_list.tasks)
        
        for i in range(len(original_todo_list.tasks)):
            assert new_todo_list.tasks[i]["task"] == original_todo_list.tasks[i]["task"]
            assert new_todo_list.tasks[i]["completed"] == original_todo_list.tasks[i]["completed"]
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_save_tasks_creates_file_if_not_exists() -> None:
    """Test that save_tasks creates the file even if it doesn't exist."""
    todo_list = TodoList()
    todo_list.add_task("Test task")
    
    # Use a path that doesn't exist yet in a temp directory
    temp_dir = tempfile.gettempdir()
    test_file = os.path.join(temp_dir, "test_tasks.json")
    
    try:
        from todo.todo_list import save_tasks
        
        # Save tasks to the new file
        save_tasks(todo_list, test_file)
        
        # Verify the file was created
        assert os.path.exists(test_file)
        
        # Verify the content
        with open(test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert len(data) == 1
        assert data[0]["task"] == "Test task"
        assert data[0]["completed"] is False
    
    finally:
        # Clean up
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_load_tasks_file_not_found() -> None:
    """Test that loading from a non-existent file raises appropriate error."""
    from todo.todo_list import load_tasks
    
    todo_list = TodoList()
    
    # Try to load from a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        load_tasks(todo_list, "non_existent_file.json")


def test_save_tasks_empty_list() -> None:
    """Test that save_tasks works with an empty todo list."""
    todo_list = TodoList()
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_filename = temp_file.name
    
    try:
        from todo.todo_list import save_tasks
        
        # Save empty list
        save_tasks(todo_list, temp_filename)
        
        # Verify the file contains an empty list
        with open(temp_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert data == []
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_tasks_persist_after_saving_and_loading() -> None:
    """Test that tasks maintain their state between save and load operations."""
    # Create a todo list with various task states
    todo_list = TodoList()
    todo_list.add_task("Pending task 1")
    todo_list.add_task("Completed task")
    todo_list.add_task("Pending task 2")
    todo_list.mark_complete("Completed task")
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
        temp_filename = temp_file.name
    
    try:
        from todo.todo_list import save_tasks, load_tasks
        
        # Save the tasks
        save_tasks(todo_list, temp_filename)
        
        # Create a fresh todo list instance
        fresh_todo_list = TodoList()
        
        # Load the tasks
        load_tasks(fresh_todo_list, temp_filename)
        
        # Verify the state is preserved
        assert len(fresh_todo_list.tasks) == 3
        
        # Check each task
        task_dict = {t["task"]: t["completed"] for t in fresh_todo_list.tasks}
        assert task_dict["Pending task 1"] is False
        assert task_dict["Completed task"] is True
        assert task_dict["Pending task 2"] is False
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)