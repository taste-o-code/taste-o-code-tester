from languages.clojure import ClojureEvalTask
import os

# Description
# Write a macro 'defargs' that similar to defn but require default values for all arguments.

task = ClojureEvalTask()
task.test_descriptions = ["Example from task description.",
                          "Example from task description.",
                          "Example from task description.",
                          "Atom as default argument.",
                          "Atom as default argument."]
