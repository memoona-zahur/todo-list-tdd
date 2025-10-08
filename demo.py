import sys
sys.path.insert(0, '.')

from todo_list import TodoList

# Create a new todo list and demonstrate functionality
todo = TodoList()

# Add tasks
todo.add_task('Buy groceries')
todo.add_task('Walk the dog')
todo.add_task('Clean the house')

print('All tasks:', todo.view_tasks())

# Mark one task as complete
todo.mark_complete(1)
print('Completed tasks:', todo.view_completed_tasks())
print('Pending tasks:', todo.view_pending_tasks())

# Update a task
todo.update_task(0, 'Buy food instead')
print('All tasks after update:', todo.view_tasks())

# Delete a task
todo.delete_task('Clean the house')
print('All tasks after deletion:', todo.view_tasks())

print('Tasks with status:', todo.view_tasks_with_status())