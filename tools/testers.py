"""Author: Andrey Malevich
This module contains different fucntions which are used to test programs
which are sent by users.
"""

from testing_exceptions import Crash
from testing_exceptions import TimeLimitExceeded
from testing_exceptions import WrongAnswer
from tools.launcher import execute_process
import logging
logging.basicConfig()

logger = logging.getLogger(__name__)

def is_timeout(exitcode):
  return exitcode == -9 or exitcode == 124

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
    task.before_test(path, test_number)
    exitcode, stdout, stderr = execute_process(task.execute_string, input, testdir = path, timelimit = task.test_timelimit)
    if exitcode != 0 and not is_timeout(exitcode):
      logger.warning('Testing crashed: %s stdout %s, stderr %s' % (exitcode, stdout, stderr))
      raise Crash("Program crashed on test #%s\n%s" % (test_number, stderr))
    elif is_timeout(exitcode):
      raise TimeLimitExceeded(test_number)
    elif not task.checker(output, stdout):
      if len(task.test_descriptions) < test_number:
        message = "Failed on test #%s" % test_number
      else:
        message = "Failed on test #%s\n%s" % (test_number, task.test_descriptions[test_number - 1])
      raise WrongAnswer(message)
    test_number += 1
