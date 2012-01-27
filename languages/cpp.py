"""
This module contains class to test C++ solutions
"""
import compilableTask
from tools.executer import execute_process

class CppTask(compilableTask.CompilableTask):
  """
  This class contains overloads of functions used specialy for testing C++ tasks
  """
  compile_string = "g++ {0}main.cpp -o {0}main.out"
  execute_string = "{0}main.out"
  filename = "main.cpp"
