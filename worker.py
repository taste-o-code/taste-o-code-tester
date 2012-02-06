from random import randint
from pyres import ResQ
import yaml

RESQUE_CONFIG = yaml.load(file('configs/resque.yml','r'))

class SubmissionChecker:

    queue = 'submissions'

    @staticmethod
    def perform(submission):
        print "Got submission"
        print submission
        result = {'id': submission['id']}

        if randint(0,1) == 0:
            result['result'] = 'accepted'
        else:
            result['result'] = 'failed'
            result['fail_cause'] = 'We are sorry'

        address = RESQUE_CONFIG['redis_resque']
        queue = RESQUE_CONFIG['queue_resque']
        worker = RESQUE_CONFIG['worker_resque']
        ResQ(address).push(queue, {'class': worker, 'args': [result]})


