from languages.clojure import ClojureEvalTask
import os

# Description
# Write a macro 'defargs' that similar to defn but require default values for all arguments.


def test_methods():
    dirname = os.path.dirname(os.path.abspath(__file__))
    test = open(os.path.join(dirname, 'test.clj'), 'r')
    return test.read()

class DerivativeTask(ClojureEvalTask):
    precode = [test_methods()]


task = DerivativeTask()
