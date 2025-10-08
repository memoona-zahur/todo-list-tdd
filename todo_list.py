"""
Todo List implementation module.
"""

from typing import List, Union, Dict, Any


class TodoList:
    """A simple todo list implementation."""

    def __init__(self) -> None:
        """Initialize an empty todo list."""
        # Changed from List[str] to List[Dict] to track completion status
        self.tasks: List[Dict[str, Union[str, bool]]] = []

    def add_task(self, task: str) -> None:
        """Add a task to the todo list."""
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self) -> List[str]:
        """Return a copy of the list of task descriptions (without completion status)."""
        return [item["task"] for item in self.tasks]

    def delete_task(self, identifier: Union[int, str]) -> str:
        """Delete a task by index or name and return the deleted task description.
        
        Args:
            identifier: Either the index of the task to delete or the name of the task to delete.
            
        Returns:
            The deleted task description.
            
        Raises:
            IndexError: If identifier is an index that's out of range.
            ValueError: If identifier is a name that doesn't exist in the list.
        """
        if isinstance(identifier, int):
            # Delete by index
            if 0 <= identifier < len(self.tasks):
                deleted_item = self.tasks.pop(identifier)
                return deleted_item["task"]
            else:
                raise IndexError("list index out of range")
        elif isinstance(identifier, str):
            # Delete by name
            for i, item in enumerate(self.tasks):
                if item["task"] == identifier:
                    deleted_item = self.tasks.pop(i)
                    return deleted_item["task"]
            else:
                raise ValueError(f"Task '{identifier}' not found")
        else:
            raise TypeError("Identifier must be an integer or string")

    def update_task(self, identifier: Union[int, str], new_task: str) -> str:
        """Update a task by index or name and return the old task description.
        
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
                old_item = self.tasks[identifier]
                old_task = old_item["task"]
                self.tasks[identifier]["task"] = new_task
                return old_task
            else:
                raise IndexError("list index out of range")
        elif isinstance(identifier, str):
            # Update by name - find the first occurrence
            for i, item in enumerate(self.tasks):
                if item["task"] == identifier:
                    old_task = item["task"]
                    item["task"] = new_task
                    return old_task
            else:
                raise ValueError(f"Task '{identifier}' not found")
        else:
            raise TypeError("Identifier must be an integer or string")

    def mark_complete(self, identifier: Union[int, str]) -> bool:
        """Mark a task as complete by index or name.
        
        Args:
            identifier: Either the index of the task to mark complete or the name of the task to mark complete.
            
        Returns:
            True if the task was marked as complete.
            
        Raises:
            IndexError: If identifier is an index that's out of range.
            ValueError: If identifier is a name that doesn't exist in the list.
        """
        if isinstance(identifier, int):
            # Mark complete by index
            if 0 <= identifier < len(self.tasks):
                self.tasks[identifier]["completed"] = True
                return True
            else:
                raise IndexError("list index out of range")
        elif isinstance(identifier, str):
            # Mark complete by name - find the first occurrence
            for i, item in enumerate(self.tasks):
                if item["task"] == identifier:
                    self.tasks[i]["completed"] = True
                    return True
            else:
                raise ValueError(f"Task '{identifier}' not found")
        else:
            raise TypeError("Identifier must be an integer or string")

    def view_completed_tasks(self) -> List[str]:
        """Return a list of completed task descriptions."""
        return [item["task"] for item in self.tasks if item["completed"]]

    def view_pending_tasks(self) -> List[str]:
        """Return a list of pending (not completed) task descriptions."""
        return [item["task"] for item in self.tasks if not item["completed"]]

    def view_tasks_with_status(self) -> List[Dict[str, Any]]:
        """Return a list of all tasks with their completion status."""
        return [{"task": item["task"], "completed": item["completed"]} for item in self.tasks]