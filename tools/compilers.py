"""Author: Andrey Malevich
This module contains different fucntions which are used to compile programs
which are sent by users.
"""
from tester_exceptions import CompilationError
from tools.launcher import execute_process

def default_compiler(task, path):
  """Compiles a task using a default compilation line for it's language.
  
  This function comiples programs which are sent by users using a default
  command line for compiling tasks of this language.
  
  Args:
    task: Task to be tested. It's assumed that task.compile_string has command
        line to compile task.
    path: Path to testing area.
  
  Returns:
    None.
  
  Raises:
    CompilationError: A compilation error accured.
  """
  exitcode, stdout, stderr = execute_process(task.compile_string.format(path))
  if exitcode: # Compilation fails if returned non-zero exit code
    raise CompilationError(stderr)
