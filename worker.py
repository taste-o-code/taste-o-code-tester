from __future__ import print_function
from random import randint
from pyres import ResQ
from executor import Executor
import yaml, os, time, config

RESQUE_CONFIG = yaml.load(file('configs/resque.yml','r'))

class SubmissionChecker(object):

  queue = "submissions"

  @staticmethod
  def perform(submission):
    result = {"id": submission["id"]}
    working_folder = os.path.join(config.PLAYGROUND_PATH, str(os.getpid())) + '/'
    if submission.has_key('destination_queue'):
      result['start_time'] = time.time()

    try:
      executor = Executor(submission["lang"].upper(), submission["task"],
          submission["source"], working_folder)
      (result["result"], result["fail_cause"]) = executor.execute()
    except ImportError as error:
      result["result"] = "failed"
      result["fail_cause"] = "We are sorry, but this language is not available."

    if submission.has_key('destination_queue'):
      queue = submission['destination_queue']
      result['finish_time'] = time.time()
    else:
      queue = RESQUE_CONFIG['queue_resque']

    worker = RESQUE_CONFIG['worker_resque']
    ResQ().push(queue, {'class': worker, 'args': [result]})

