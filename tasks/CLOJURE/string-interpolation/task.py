from languages.clojure import ClojureEvalTask

# Description
# Write << macro for string interpolation

task = ClojureEvalTask()

task.test_descriptions = ["First example from task description.",
                          "Second example from task description.",
                          "Many nested s-exps inside interpolated s-exp.",
                          "Third example from task description.",
                          "Fourth example from task description.",
                          "Checks that all passed strings in macro are concatenated."]

