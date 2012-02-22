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
      clean_directory(path)
      task.create_files(path)
      task.compile(path)
      task.test(path)
    except CompilationError as exception:
      return ("failed", "Compilation error: " + unicode(exception))
    except Crash as exception:
      return ("failed", "Crash: " + unicode(exception))
    except TimeLimitExceeded as exception:
      return ("failed", unicode(exception))
    except WrongAnswer as exception:
      return ("failed", "Wrong Answer: " + unicode(exception))
    except TesterFailed as exception:
      return ("failed", "Out tester failed on: " + unicode(exception))
    except CompilationLimitExceeded as exception:
      return ("failed", "Compilation limit exceeded")
    else:
      return ("accepted", None)

