from random import randint
from pyres import ResQ

REDIS_RESQUE = "localhost:6379"

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

        ResQ(REDIS_RESQUE).push('submission_results',
                                {'class': 'SubmissionResultHandler', 'args': [result]})


