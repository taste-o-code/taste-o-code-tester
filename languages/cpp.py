"""
This module contains class to test C++ solutions
"""
from compilable_task import CompilableTask
from tools.file_creators import create_solution_and_copy_checker

class CppTask(CompilableTask):
  """
  This class contains overloads of functions used specialy for testing C++ tasks
  """
  compile_strings = ["g++ {0}/main.cpp -o {0}/main.out"]
  execute_string = "{0}/main.out"
  filenames = ["main.cpp"]

class CppTaskWithChecker(CompilableTask):

  checker_file = "checker.cpp"
  filename = "solution.cpp"
  compile_strings = ["g++ {0}/solution.cpp {0}/checker.cpp -o {0}/main.out"]
  execute_string = "{0}/main.out"

  def __init__(self):
    CompilableTask.__init__(self, create_files = create_solution_and_copy_checker)

