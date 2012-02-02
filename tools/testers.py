import exceptions
from tools.launcher import execute_process

def default_tester(task, path):
  checker = task.checker
  test_number = 0
  for input, output in task.tests:
    exitcode, stdout, stderr = execute_process(task.execute_string.format(path),
      input)
    if exitcode != 0:
      raise exceptions.Crash("Program exited with code " + str(exitcode))
    elif not checker(output, stdout):
      raise exceptions.WrongAnswer("Failed on test number: " + str(test_number))
    test_number += 1
