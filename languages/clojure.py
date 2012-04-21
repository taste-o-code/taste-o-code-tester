from task import Task

SANDBOX_FILES_PATH = '/home/playground/sandbox-files/'


class ClojureTask(Task):

    execute_string = "java -Djava.security.manager -Xmx140m -Djava.security.policy={0}java.policy -cp {0}clojure-1.4.0.jar clojure.main {{0}}solution.clj".format(SANDBOX_FILES_PATH)
    filenames = ["solution.clj"]

class ClojureEvalTask(ClojureTask):
    postcode = ["(load-reader *in*)"]

