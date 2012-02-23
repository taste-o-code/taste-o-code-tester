from __future__ import print_function
from tools.testing_exceptions import *
from tools.preparator import *

class Executor:
  def __init__(self, language, task_id, sources, path):
    self.task = get_task(language, task_id)
    self.path = path
    self.task.sources = sources
    
  def execute(self):
    task = self.task
    path = self.path
    try:
      prepare_directory(path)
      task.create_files(path)
      task.compile(path)
      task.test(path)
    except CompilationLimitExceeded as exception:
      result = ("failed", "Compilation time limit exceeded.")
    except CompilationError as exception:
      result = ("failed", "Compilation error: " + unicode(exception))
    except Crash as exception:
      result = ("failed", "Crash: " + unicode(exception))
    except TimeLimitExceeded as exception:
      result = ("failed", unicode(exception))
    except WrongAnswer as exception:
      result = ("failed", "Wrong Answer: " + unicode(exception))
    except TesterFailed as exception:
      result = ("failed", "Out tester failed on: " + unicode(exception))
    else:
      result =  ("accepted", None)
    cleanup(path)
    return result

