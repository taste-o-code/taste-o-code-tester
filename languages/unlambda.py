from __future__ import print_function
from task import Task
from tools.launcher import execute_process
from tools.testing_exceptions import Crash
from tools.testing_exceptions import TimeLimitExceeded
from tools.testing_exceptions import WrongAnswer
import config, os, codecs, logging

logger = logging.getLogger(__name__)

def substitute_and_write_solution(template, source, path):
  replaced = template.replace('%', source)
  solution_file = codecs.open(path, mode='w', encoding='utf-8')
  print(replaced, file = solution_file, end = "")
  solution_file.close()


def unlambda_tester(task, path):
  solution_file = os.path.join(path, task.filenames[0])
  test_number = 1
  for template, output in task.tests:
    substitute_and_write_solution(template, task.source, solution_file)
    exitcode, stdout, stderr = execute_process(task.execute_string.format(path))
    if exitcode != 0 and exitcode != -9:
      logger.warning('Testing crashed: %s' % stderr)
      raise Crash("Program crashed on test #%s" % test_number)
    elif exitcode == -9:
      raise TimeLimitExceeded()
    elif not task.checker(output, stdout):
      raise WrongAnswer("Failed on test #%s" % test_number)
    test_number += 1

"""
   Unlambda tasks have testing workflow different from other languages.
   Usually we have  1 solution file and run it against set of test files.
   In unlambda every test consist of a template and expected output. Template is a text: program in unlambda with % placeholder.
   % placeholder is replaced with user's solution and then we call unlambda on this file.
   This way we can call user's function with different arguments for every test.
   So input files become template files and output files stay output.
"""
class UnlambdaTask(Task):

    def __init__(self):
        super(UnlambdaTask, self).__init__(tester = unlambda_tester)

    execute_string = "{0}/unlambda {{0}}/solution.unl".format(config.PLAYGROUND_FILES_PATH)
    filenames = ["solution.unl"]

