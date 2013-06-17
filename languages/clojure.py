from task import Task
import config

class ClojureTask(Task):

    test_timelimit = 10 # clojure startup is slow :(

    execute_string = "java -Djava.security.manager -Xmx140m -Djava.security.policy={0}/java.policy -cp {0}/clojure-1.5.1.jar clojure.main solution.clj".format(config.PLAYGROUND_FILES_PATH)
    filenames = ["solution.clj"]

class ClojureEvalTask(ClojureTask):
    postcode = ["(load-reader *in*)"]

