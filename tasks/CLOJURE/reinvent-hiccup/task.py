from languages.clojure import ClojureEvalTask
import os

# Description
# Write a function `html` to simulate Hiccup library https://github.com/weavejester/hiccup.


def get_precode():
    dirname = os.path.dirname(os.path.abspath(__file__))
    test = open(os.path.join(dirname, 'precode.clj'), 'r')
    return test.read()

class ReinventHiccupTask(ClojureEvalTask):
    precode = [get_precode()]


task = ReinventHiccupTask()

task.test_descriptions = ["Checks empty empty tag.",
                          "Checks nested tags that might contain strings.",
                          "Checks nested tags that might contain strings.",
                          "Checks tag that contains collection (non vector).",
                          "Checks tags that contain map of attributes.",
                          "Checks tags that contain map of attributes.",
                          "Checks simple tag."]
