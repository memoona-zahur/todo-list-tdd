"""
Todo List implementation module.
"""

from typing import List, Union


class TodoList:
    """A simple todo list implementation."""

    def __init__(self) -> None:
        """Initialize an empty todo list."""
        self.tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """Add a task to the todo list."""
        self.tasks.append(task)

    def view_tasks(self) -> List[str]:
        """Return a copy of the list of tasks."""
        return self.tasks.copy()

    def delete_task(self, identifier: Union[int, str]) -> str:
        """Delete a task by index or name and return the deleted task.
        
        Args:
            identifier: Either the index of the task to delete or the name of the task to delete.
            
        Returns:
            The deleted task.
            
        Raises:
            IndexError: If identifier is an index that's out of range.
            ValueError: If identifier is a name that doesn't exist in the list.
        """
        if isinstance(identifier, int):
            # Delete by index
            if 0 <= identifier < len(self.tasks):
                return self.tasks.pop(identifier)
            else:
                raise IndexError("list index out of range")
        elif isinstance(identifier, str):
            # Delete by name
            if identifier in self.tasks:
                index = self.tasks.index(identifier)
                return self.tasks.pop(index)
            else:
                raise ValueError(f"Task '{identifier}' not found")
        else:
            raise TypeError("Identifier must be an integer or string")

    def update_task(self, identifier: Union[int, str], new_task: str) -> str:
        """Update a task by index or name and return the old task.
        
        Args:
            identifier: Either the index of the task to update or the name of the task to update.
            new_task: The new task description to replace the old one.
            
        Returns:
            The old task that was replaced.
            
        Raises:
            IndexError: If identifier is an index that's out of range.
            ValueError: If identifier is a name that doesn't exist in the list.
        """
        if isinstance(identifier, int):
            # Update by index
            if 0 <= identifier < len(self.tasks):
                old_task = self.tasks[identifier]
                self.tasks[identifier] = new_task
                return old_task
            else:
                raise IndexError("list index out of range")
        elif isinstance(identifier, str):
            # Update by name - find the first occurrence
            if identifier in self.tasks:
                index = self.tasks.index(identifier)
                old_task = self.tasks[index]
                self.tasks[index] = new_task
                return old_task
            else:
                raise ValueError(f"Task '{identifier}' not found")
        else:
            raise TypeError("Identifier must be an integer or string")
