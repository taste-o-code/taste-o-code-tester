"""
This module contains class to test Python solutions
"""
import task
from tools.executer import execute_process

class PythonTask(task.Task):
  """
  This class contains overloads of functions used specialy for testing Python tasks
  """
  execute_string = "python {0}main.py"
  filename = "main.py"