"""
Command Line Interface for the Todo List application.
"""

import argparse
import sys
from typing import List, Union
from todo.todo_list import TodoList, save_tasks, load_tasks
import os


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="A simple command line todo list application.",
        prog="todo"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task to add")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--completed", 
        action="store_true", 
        help="Show only completed tasks"
    )
    list_parser.add_argument(
        "--pending", 
        action="store_true", 
        help="Show only pending tasks"
    )
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument(
        "identifier", 
        type=str, 
        help="The task name or index (0-based) to delete"
    )
    
    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument(
        "identifier", 
        type=str, 
        help="The task name or index (0-based) to update"
    )
    update_parser.add_argument(
        "new_task", 
        type=str, 
        help="The new task description"
    )
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument(
        "identifier", 
        type=str, 
        help="The task name or index (0-based) to mark complete"
    )
    
    return parser


def handle_add(todo_list: TodoList, args: argparse.Namespace) -> None:
    """Handle the add command."""
    todo_list.add_task(args.task)
    print(f"Added task: {args.task}")


def handle_list(todo_list: TodoList, args: argparse.Namespace) -> None:
    """Handle the list command."""
    if args.completed:
        tasks = todo_list.view_completed_tasks()
        print("Completed tasks:")
        for i, task in enumerate(tasks):
            print(f"  {i}. {task}")
    elif args.pending:
        tasks = todo_list.view_pending_tasks()
        print("Pending tasks:")
        for i, task in enumerate(tasks):
            print(f"  {i}. {task}")
    else:
        all_tasks = todo_list.view_tasks_with_status()
        if not all_tasks:
            print("No tasks in the list.")
            return
            
        print("All tasks:")
        for i, task_data in enumerate(all_tasks):
            status = "X" if task_data["completed"] else "O"
            print(f"  {i}. [{status}] {task_data['task']}")


def handle_delete(todo_list: TodoList, args: argparse.Namespace) -> None:
    """Handle the delete command."""
    identifier = parse_identifier(args.identifier)
    deleted_task = todo_list.delete_task(identifier)
    print(f"Deleted task: {deleted_task}")


def handle_update(todo_list: TodoList, args: argparse.Namespace) -> None:
    """Handle the update command."""
    identifier = parse_identifier(args.identifier)
    old_task = todo_list.update_task(identifier, args.new_task)
    print(f"Updated task: '{old_task}' -> '{args.new_task}'")


def handle_complete(todo_list: TodoList, args: argparse.Namespace) -> None:
    """Handle the complete command."""
    identifier = parse_identifier(args.identifier)
    todo_list.mark_complete(identifier)
    # Get the task that was marked complete to display it
    if isinstance(identifier, int):
        tasks = todo_list.view_tasks()
        completed_task = tasks[identifier] if 0 <= identifier < len(tasks) else "unknown task"
    else:
        completed_task = identifier  # If it was a string, that's the task name
    print(f"Marked task as complete: {completed_task}")


def parse_identifier(identifier_str: str) -> Union[int, str]:
    """Parse the identifier to determine if it's an index or a task name."""
    try:
        return int(identifier_str)
    except ValueError:
        return identifier_str


def main() -> None:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize the todo list
    todo_list = TodoList()
    
    # Define the data file path
    data_file = "todo_data.json"
    
    # Load existing data if file exists and is not empty
    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        try:
            load_tasks(todo_list, data_file)
        except Exception as e:
            print(f"Warning: Could not load existing tasks: {e}")
            print("Starting with an empty list.")
    
    # Handle commands
    
    if args.command == "add":
        handle_add(todo_list, args)
    elif args.command == "list":
        handle_list(todo_list, args)
    elif args.command == "delete":
        handle_delete(todo_list, args)
    elif args.command == "update":
        handle_update(todo_list, args)
    elif args.command == "complete":
        handle_complete(todo_list, args)
    else:
        parser.print_help()
        sys.exit(1)

    # Save tasks after handling any command that might modify the todo list
    if args.command in ["add", "delete", "update", "complete"]:
        try:
            save_tasks(todo_list, data_file)
        except Exception as e:
            print(f"Warning: Could not save tasks: {e}")


if __name__ == "__main__":
    main()