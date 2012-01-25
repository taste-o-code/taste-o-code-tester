"""
This module contains class to test Java solutions
"""
import task
from tools.executer import execute_process

class JavaTask(task.Task):
  """
  This class contains overloads of functions used specialy for testing Java tasks
  """
  compile_string = "javac {0}Main.java"
  execute_string = "java {0}Main"

  def compile(self):
    result = execute_process(self.compile_string.format(self.path))
    return result
  
  def create_files(self):
    source_file = open("./{0}Main.java", "w")
    [print(line, file = source_file, end = "") for line in self.source]
    source_file.close()