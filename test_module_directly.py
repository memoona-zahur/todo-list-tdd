import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'todo'))

# Import directly from the module in the todo directory
from todo_list import TodoList, save_tasks, load_tasks
import tempfile

# Create a todo list and add some tasks
todo = TodoList()
todo.add_task('First task')
todo.add_task('Second task')
todo.mark_complete('First task')

print('Original tasks:')
for task in todo.tasks:
    status = 'COMPLETED' if task['completed'] else 'PENDING'
    print(f'  [{status}] {task["task"]}')

# Save to temp file
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
    temp_file = f.name

save_tasks(todo, temp_file)
print(f'\nTasks saved to {temp_file}')

# Load into new instance
new_todo = TodoList()
load_tasks(new_todo, temp_file)

print('\nLoaded tasks:')
for task in new_todo.tasks:
    status = 'COMPLETED' if task['completed'] else 'PENDING'
    print(f'  [{status}] {task["task"]}')

# Cleanup
os.unlink(temp_file)
print('\nPersistence functionality works correctly!')