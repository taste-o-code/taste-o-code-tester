"""Author: Andrey Malevich
This module contains different fucntions which are used to test programs
which are sent by users.
"""

from testing_exceptions import Crash
from testing_exceptions import TimeLimitExceeded
from testing_exceptions import WrongAnswer
from tools.launcher import execute_process

def default_tester(task, path):
  """Tests a user's solution of the task using a default execution line for
  task's language.
  
  This function tests solutions which are sent by users using a default
  command line for executing tasks of this language.
  
  Args:
    task: Task to be tested. It's assumed that task.execute_string has command
        line to execute a solution.
    path: Path to testing area.
  
  Returns:
    None.
  
  Raises:
    Crash: User's solution crashed.
    WrongAnswer: User's solution returned a wrong answer.
  """
  test_number = 1
  for input, output in task.tests:
    exitcode, stdout, stderr = execute_process(task.execute_string.format(path),
      input)
    if exitcode != 0 and exitcode != -9:
      raise Crash("Program exited with code " + str(exitcode))
    elif exitcode == -9:
      raise TimeLimitExceeded()
    elif not task.checker(output, stdout):
      raise WrongAnswer("Failed on test number: " + str(test_number))
    test_number += 1
