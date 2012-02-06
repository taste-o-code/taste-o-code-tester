"""Author: Andrey Malevich
This module contains different fucntions which are used to test programs
which are sent by users.
"""

import exceptions
from tools.launcher import execute_process

def default_tester(task, path):
  """Tests a users solution of the task using a default execution line for
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
    Crash: User's solution have crashed.
    WrongAnswer: User's solution have return a wrong answer.
  """
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
