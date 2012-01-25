"""
This module contains class to test C++ solutions
"""
import task
from tools.executer import execute_process

class CppTask(task.Task):
  """
  This class contains overloads of functions used specialy for testing C++ tasks
  """
  compile_string = "g++ {0}main.cpp -o {0}main.out"
  execute_string = "./{0}main.out"
#  checker = ignore_whitespace_check

  def compile(self):
    result = execute_process(self.compile_string.format(self.path))
    return result
  
  def create_files(self):
    source_file = open("./{0}main.cpp".format(self.path), "w")
    [print(line, file = source_file, end = "") for line in self.source]
    source_file.close()