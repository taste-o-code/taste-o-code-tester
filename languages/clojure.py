from task import Task
import config

class ClojureTask(Task):

    execute_string = "java -Djava.security.manager -Xmx140m -Djava.security.policy={0}/java.policy -cp {0}/clojure-1.4.0.jar clojure.main {{0}}solution.clj".format(config.PLAYGROUND_FILES_PATH)
    filenames = ["solution.clj"]

class ClojureEvalTask(ClojureTask):
    postcode = ["(load-reader *in*)"]

