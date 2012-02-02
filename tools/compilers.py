import exceptions
from tools.launcher import execute_process

def default_compiler(task, path):
  exitcode, stdout, stderr = execute_process(task.compile_string.format(path))
  if exitcode: # Compilation fails if returned non-zero exit code
    raise exceptions.CompilationError(stderr)
