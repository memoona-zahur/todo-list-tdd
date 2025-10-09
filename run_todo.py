"""
Script to run the todo list CLI application.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from todo.cli import main

if __name__ == "__main__":
    main()