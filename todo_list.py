"""
Todo List implementation module.
"""
from typing import List


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
