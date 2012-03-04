from __future__ import print_function
from random import randint
from pyres import ResQ
from executor import Executor
import yaml, os

RESQUE_CONFIG = yaml.load(file('configs/resque.yml','r'))
path = "/home/playground/0"

class SubmissionChecker(object):

  queue = "submissions"

  @staticmethod
  def perform(submission):
    print("Got submission")
    print(submission)
    result = {"id": submission["id"]}
    working_folder = os.path.join(path, str(os.getpid())) + '/'
    try:
      executor = Executor(submission["lang"].upper(), str(submission["task"]),
          submission["source"], working_folder)
      (result["result"], result["fail_cause"]) = executor.execute()
    except ImportError as error:
      result["result"] = "failed"
      result["fail_cause"] = "We are sorry, but this language is not available."

    queue = RESQUE_CONFIG['queue_resque']
    worker = RESQUE_CONFIG['worker_resque']
    ResQ().push(queue, {'class': worker, 'args': [result]})

