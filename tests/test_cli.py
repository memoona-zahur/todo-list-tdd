"""
Unit tests for the CLI functionality.
Following TDD: Write tests first, implement code after.
"""

import sys
from io import StringIO
from unittest.mock import patch, Mock
import pytest
from todo.cli import main


def test_cli_add_command() -> None:
    """Test that the CLI add command works correctly."""
    # Simulate command line arguments
    test_args = ["todo", "add", "Buy groceries"]
    
    with patch('sys.argv', test_args):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with patch('todo_list.TodoList'):
                # Run the CLI main function
                result = main()
                # The main function should return None
                assert result is None


def test_cli_list_command() -> None:
    """Test that the CLI list command works correctly."""
    # Simulate command line arguments
    test_args = ["todo", "list"]
    
    with patch('sys.argv', test_args):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with patch('todo_list.TodoList'):
                # Run the CLI main function
                result = main()
                # The main function should return None
                assert result is None


def test_cli_delete_command() -> None:
    """Test that the CLI delete command works correctly."""
    # Simulate command line arguments
    test_args = ["todo", "delete", "0"]
    
    with patch('sys.argv', test_args):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with patch('todo.cli.TodoList') as mock_todo_list_class:
                mock_instance = Mock()
                mock_todo_list_class.return_value = mock_instance
                mock_instance.delete_task.return_value = "Test task"
                
                # Run the CLI main function
                result = main()
                # The main function should return None
                assert result is None


def test_cli_update_command() -> None:
    """Test that the CLI update command works correctly."""
    # Simulate command line arguments
    test_args = ["todo", "update", "0", "Updated task"]
    
    with patch('sys.argv', test_args):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with patch('todo.cli.TodoList') as mock_todo_list_class:
                mock_instance = Mock()
                mock_todo_list_class.return_value = mock_instance
                mock_instance.update_task.return_value = "Old task"
                
                # Run the CLI main function
                result = main()
                # The main function should return None
                assert result is None


def test_cli_complete_command() -> None:
    """Test that the CLI complete command works correctly."""
    # Simulate command line arguments
    test_args = ["todo", "complete", "0"]
    
    with patch('sys.argv', test_args):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with patch('todo.cli.TodoList') as mock_todo_list_class:
                mock_instance = Mock()
                mock_todo_list_class.return_value = mock_instance
                mock_instance.mark_complete.return_value = True
                mock_instance.view_tasks.return_value = ["Test task"]  # Mock the view_tasks method as well
                
                # Run the CLI main function
                result = main()
                # The main function should return None
                assert result is None


def test_cli_invalid_command() -> None:
    """Test that the CLI handles invalid commands gracefully."""
    # Simulate command line arguments
    test_args = ["todo", "invalidcommand"]
    
    with patch('sys.argv', test_args):
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            with patch('todo_list.TodoList'):
                # Run the CLI main function
                with pytest.raises(SystemExit):  # argparse typically exits on invalid command
                    main()


def test_cli_add_task_through_cli() -> None:
    """Test that adding a task through CLI works."""
    # This test will check if the add functionality is properly connected to the TodoList
    test_args = ["todo", "add", "Test task"]
    
    with patch('sys.argv', test_args):
        # Mock the TodoList and its add_task method
        with patch('todo.cli.TodoList') as mock_todo_list_class:
            mock_instance = Mock()
            mock_todo_list_class.return_value = mock_instance
            
            # Run the CLI main function
            main()
            
            # Verify that add_task was called with the correct argument
            mock_instance.add_task.assert_called_once_with("Test task")


def test_cli_list_tasks_through_cli() -> None:
    """Test that listing tasks through CLI works."""
    # This test will check if the list functionality is properly connected to the TodoList
    test_args = ["todo", "list"]
    
    with patch('sys.argv', test_args):
        # Mock the TodoList and its view_tasks method
        with patch('todo.cli.TodoList') as mock_todo_list_class:
            mock_instance = Mock()
            mock_todo_list_class.return_value = mock_instance
            mock_instance.view_tasks_with_status.return_value = [{"task": "Task 1", "completed": False}, {"task": "Task 2", "completed": True}]
            
            # Capture stdout to verify the output
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                # Run the CLI main function
                main()
                
                # Verify that view_tasks_with_status was called
                mock_instance.view_tasks_with_status.assert_called_once()


def test_cli_delete_task_by_index_through_cli() -> None:
    """Test that deleting a task by index through CLI works."""
    # This test will check if the delete functionality is properly connected to the TodoList
    test_args = ["todo", "delete", "0"]
    
    with patch('sys.argv', test_args):
        # Mock the TodoList and its delete_task method
        with patch('todo.cli.TodoList') as mock_todo_list_class:
            mock_instance = Mock()
            mock_todo_list_class.return_value = mock_instance
            mock_instance.delete_task.return_value = "Deleted task"
            
            # Run the CLI main function
            main()
            
            # Verify that delete_task was called with the correct argument
            mock_instance.delete_task.assert_called_once_with(0)


def test_cli_delete_task_by_name_through_cli() -> None:
    """Test that deleting a task by name through CLI works."""
    # This test will check if the delete functionality is properly connected to the TodoList
    test_args = ["todo", "delete", "Task to delete"]
    
    with patch('sys.argv', test_args):
        # Mock the TodoList and its delete_task method
        with patch('todo.cli.TodoList') as mock_todo_list_class:
            mock_instance = Mock()
            mock_todo_list_class.return_value = mock_instance
            mock_instance.delete_task.return_value = "Task to delete"
            
            # Run the CLI main function
            main()
            
            # Verify that delete_task was called with the correct argument
            mock_instance.delete_task.assert_called_once_with("Task to delete")