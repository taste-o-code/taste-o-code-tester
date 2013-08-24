from languages.clojure import ClojureEvalTask
import os

# Description
# Write a function `derivative` to calculate derivative of a given expression.


def test_methods():
    dirname = os.path.dirname(os.path.abspath(__file__))
    test = open(os.path.join(dirname, 'test.clj'), 'r')
    return test.read()

class DerivativeTask(ClojureEvalTask):
    precode = [test_methods()]


task = DerivativeTask()

task.test_descriptions = ["Checks contstant.",
                          "Checks x.",
                          "Checks addition.",
                          "Checks subtraction.",
                          "Checks multiplication.",
                          "Checks division.",
                          "Checks complex expression with divisions, additions, multiplications and subtractions.",
                          "Checks second derivative of complex expression."]
