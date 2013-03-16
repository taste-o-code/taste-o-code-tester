from languages.cpp import CppTaskWithChecker
from tools.checkers import checker_floats
from tools.testing_exceptions import Crash, TimeLimitExceeded, WrongAnswer
from tools.launcher import execute_process
import shutil
import os
import logging

def is_timeout(exitcode):
  return exitcode == -9 or exitcode == 124

def copy_bin_tester(task, path):
  test_number = 1
  for input, output in task.tests:
    data_file = os.path.join(task.directory, '%02d.bin' % (test_number - 1))
    shutil.copy(data_file, os.path.join(path, 'data.bin'))
    exitcode, stdout, stderr = execute_process(task.execute_string.format(path),
      input, testdir = path)
    if exitcode != 0 and not is_timeout(exitcode):
      logging.warning('Testing crashed: %s stdout %s, stderr %s' % (exitcode, stdout, stderr))
      raise Crash('Program crashed on test #%s' % test_number)
    elif is_timeout(exitcode):
      raise TimeLimitExceeded()
    elif not task.checker(output, stdout):
      raise WrongAnswer('Failed on test #%s' % test_number)
    test_number += 1


# Write method 'averageGrades' that calculates average grades in each group.
task = CppTaskWithChecker()
task.checker = checker_floats
task.test = copy_bin_tester.__get__(task)

