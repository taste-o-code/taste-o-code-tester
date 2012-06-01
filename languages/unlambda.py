from task import Task
import config

class UnlambdaTask(Task):

    execute_string = "{0}/unlambda {{0}}solution.unl".format(config.PLAYGROUND_FILES_PATH)
    filenames = ["solution.unl"]

