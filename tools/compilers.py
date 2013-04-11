"""Author: Andrey Malevich
This module contains different fucntions which are used to compile programs
which are sent by users.
"""
from testing_exceptions import CompilationError
from testing_exceptions import CompilationLimitExceeded
from tools.launcher import execute_process


def compile(compile_string, path):
  """ Runs given string and raises exception if it returned any error. """
  exitcode, stdout, stderr = execute_process(compile_string, testdir = path)
  if exitcode: # Compilation fails if returned non-zero exit code
    if exitcode != -9:
      raise CompilationError(stderr)
    else:
      raise CompilationLimitExceeded()



def default_compiler(task, path):
  """Compiles a task using a default compilation line for it's language.

  This function comiples programs which are sent by users using a default
  command line for compiling tasks of this language.

  Args:
    task: Task to be tested. It's assumed that task.compile_strings is a list of command for compiling.
    path: Path to testing area.

  Returns:
    None.

  Raises:
    CompilationError: A compilation error accured.
  """
  for compile_string in task.compile_strings:
    compile(compile_string, path)
