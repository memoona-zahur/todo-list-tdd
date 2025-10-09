# Todo List TDD

A simple, command-line-based todo list application built using Test-Driven Development (TDD) methodology. This application allows users to manage their tasks through a comprehensive set of features including adding, deleting, updating, and marking tasks as complete.

## Features

- **Add Tasks**: Add new tasks to your todo list
- **Delete Tasks**: Remove tasks by name or index
- **Update Tasks**: Modify existing task descriptions
- **Mark Complete**: Track completed tasks
- **View Tasks**: See all tasks, completed tasks, or pending tasks separately
- **Persistent Storage**: Tasks are saved to and loaded from a JSON file (`todo_data.json`)
- **Command Line Interface**: Easy-to-use CLI for managing tasks
- **Comprehensive Testing**: Built with TDD approach, ensuring reliable functionality

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.12+ installed on your system
3. Install the package in development mode:

```bash
pip install -e .
```

## Usage

### Command Line Interface

The application provides a command-line interface for easy task management:

#### Add a task
```bash
python -m todo.cli add "My new task"
```

#### List all tasks
```bash
python -m todo.cli list
```

#### List completed tasks only
```bash
python -m todo.cli list --completed
```

#### List pending tasks only
```bash
python -m todo.cli list --pending
```

#### Delete a task
```bash
# Delete by task name
python -m todo.cli delete "My task"

# Delete by index (0-based)
python -m todo.cli delete 0
```

#### Update a task
```bash
# Update by task name
python -m todo.cli update "Old task name" "New task description"

# Update by index (0-based)
python -m todo.cli update 0 "New task description"
```

#### Mark a task as complete
```bash
# Complete by task name
python -m todo.cli complete "My task"

# Complete by index (0-based)
python -m todo.cli complete 0
```

### Programmatic Usage

You can also use the `TodoList` class directly in your Python code:

```python
from todo.todo_list import TodoList

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
```

### Data Persistence

Tasks are automatically saved to `todo_data.json` after each modification and loaded when the CLI is started. The data is stored in JSON format:

```json
[
  {
    "task": "Sample task",
    "completed": false
  }
]
```

## Project Structure

```
todo-list-tdd/
├── demo.py                 # Demo script showing programmatic usage
├── hello.py                # Simple hello world script
├── pyproject.toml          # Project configuration and dependencies
├── README.md              # This file
├── todo_data.json         # Persistent storage for tasks
├── todo/                  # Main application package
│   ├── __init__.py        # Package initialization
│   ├── todo_list.py       # Core TodoList class implementation
│   └── cli.py             # Command-line interface
└── tests/                 # Test suite
    ├── test_cli.py
    ├── test_delete_task.py
    ├── test_mark_complete.py
    ├── test_todo_list.py
    ├── test_update_task.py
    └── test_view_tasks.py
```

## Running Tests

The project uses pytest for testing. All tests follow TDD principles:

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=todo

# Run specific test file
python -m pytest tests/test_todo_list.py
```

## Testing Philosophy

This project was developed following Test-Driven Development principles:

1. Write tests for a feature before implementing the feature
2. Run the test to ensure it fails (red phase)
3. Implement the minimum code necessary to make the test pass (green phase)
4. Refactor the code while ensuring tests still pass (refactor phase)
5. Repeat for the next feature

This approach ensures:

- High test coverage
- Reliable functionality
- Clean, maintainable code
- Clear specification of expected behavior

## API Documentation

### TodoList Class

#### `add_task(task: str) -> None`
Add a task to the todo list.

#### `view_tasks() -> List[str]`
Return a list of all task descriptions without completion status.

#### `delete_task(identifier: Union[int, str]) -> str`
Delete a task by index or name and return the deleted task description.

#### `update_task(identifier: Union[int, str], new_task: str) -> str`
Update a task by index or name and return the old task description.

#### `mark_complete(identifier: Union[int, str]) -> bool`
Mark a task as complete by index or name.

#### `view_completed_tasks() -> List[str]`
Return a list of completed task descriptions.

#### `view_pending_tasks() -> List[str]`
Return a list of pending (not completed) task descriptions.

#### `view_tasks_with_status() -> List[Dict[str, Any]]`
Return a list of all tasks with their completion status.

### Utility Functions

#### `save_tasks(todo_list: TodoList, filename: str) -> None`
Save tasks to a JSON file.

#### `load_tasks(todo_list: TodoList, filename: str) -> None`
Load tasks from a JSON file.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following TDD principles (write tests first)
4. Run the tests to ensure everything passes
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- Task categories or tags
- Due dates for tasks
- Priority levels
- Export functionality (CSV, PDF)
- Web interface
- Multi-user support

## Troubleshooting

If you encounter issues running the CLI commands:

1. Ensure you're using the correct module path: `python -m todo.cli`
2. Make sure the package is installed in development mode: `pip install -e .`
3. Check that `todo_data.json` has the correct permissions for read/write access

## Acknowledgments

This project demonstrates the practical application of Test-Driven Development in Python, creating a robust and reliable todo list application with comprehensive test coverage.