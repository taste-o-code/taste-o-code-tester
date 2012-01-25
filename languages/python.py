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
  
  def create_files(self):
    source_file = open("./{0}main.py".format(self.path), "w")
    [print(line, file = source_file, end = "") for line in self.source]
    source_file.close()