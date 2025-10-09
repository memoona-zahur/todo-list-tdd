"""
Demo script to test persistence functionality between sessions.
"""
from todo.todo_list import TodoList, save_tasks, load_tasks
import os

def session_1():
    """Simulate first session - create tasks and save them."""
    print("=== Session 1: Creating and saving tasks ===")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Add some tasks
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Walk the dog")
    todo_list.add_task("Clean the house")
    
    # Mark one as complete
    todo_list.mark_complete("Walk the dog")
    
    # Show current tasks
    print("Current tasks:")
    for i, task in enumerate(todo_list.tasks):
        status = "[COMPLETED]" if task["completed"] else "[PENDING]"
        print(f"  {status} {task['task']}")
    
    # Save tasks to file
    save_tasks(todo_list, "tasks.json")
    print("\nTasks saved to tasks.json")
    

def session_2():
    """Simulate second session - load tasks from file."""
    print("\n=== Session 2: Loading tasks from file ===")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Load tasks from file
    load_tasks(todo_list, "tasks.json")
    
    # Show loaded tasks
    print("Loaded tasks:")
    for i, task in enumerate(todo_list.tasks):
        status = "[COMPLETED]" if task["completed"] else "[PENDING]"
        print(f"  {status} {task['task']}")
    
    # Add a new task in this session
    todo_list.add_task("Do laundry")
    
    # Save updated tasks
    save_tasks(todo_list, "tasks.json")
    print("\nUpdated tasks saved to tasks.json")


def session_3():
    """Simulate third session - verify updated tasks were saved."""
    print("\n=== Session 3: Verifying persistent data ===")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Load tasks from file
    load_tasks(todo_list, "tasks.json")
    
    # Show loaded tasks
    print("Loaded tasks (with the new 'Do laundry' task):")
    for i, task in enumerate(todo_list.tasks):
        status = "[COMPLETED]" if task["completed"] else "[PENDING]"
        print(f"  {status} {task['task']}")
    
    # Clean up
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
        print("\nCleaned up tasks.json")


if __name__ == "__main__":
    session_1()
    session_2()
    session_3()
    print("\nPersistence test completed successfully!")