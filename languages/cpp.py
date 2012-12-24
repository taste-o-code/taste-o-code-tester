"""
This module contains class to test C++ solutions
"""
from compilable_task import CompilableTask

class CppTask(CompilableTask):
  """
  This class contains overloads of functions used specialy for testing C++ tasks
  """
  compile_strings = ["g++ {0}/main.cpp -o {0}/main.out"]
  execute_string = "{0}/main.out"
  filenames = ["main.cpp"]
