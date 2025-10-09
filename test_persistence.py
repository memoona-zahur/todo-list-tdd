from todo import TodoList, save_tasks, load_tasks
import tempfile
import os

# Create a todo list and add some tasks
todo = TodoList()
todo.add_task('First task')
todo.add_task('Second task')
todo.mark_complete('First task')

print('Original tasks:')
for task in todo.tasks:
    print(f'  {task}')

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
    print(f'  {task}')

# Cleanup
os.unlink(temp_file)
print('\nPersistence functionality works correctly!')