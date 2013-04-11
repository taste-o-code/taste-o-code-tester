"""
This module contains class to test C++ solutions
"""
from compilable_task import CompilableTask
from tools.file_creators import create_solution_and_copy_checker

class CppTask(CompilableTask):
  """
  This class contains overloads of functions used specialy for testing C++ tasks
  """
  compile_strings = ["g++ main.cpp -o main.out"]
  execute_string = "./main.out"
  filenames = ["main.cpp"]

class CppTaskWithChecker(CompilableTask):

  checker_file = "checker.cpp"
  filename = "solution.cpp"
  compile_strings = ["g++ solution.cpp checker.cpp -o main.out"]
  execute_string = "./main.out"

  def __init__(self):
    CompilableTask.__init__(self, create_files = create_solution_and_copy_checker)

