from languages.java import JavaTask

# Description
# Implement Promise class that implements java.util.concurrent.Future and allows to set value.

task = JavaTask()
task.set_solution_class_name("Promise")
task.test_descriptions = ["Check normal flow: delayed set() then get() in separate thread.",
                          "Check get with timeout when timeout is not reached.",
                          "Check get with timeout when timeout is reached and exception must be thrown.",
                          "Check multiple set() invocation.",
                          "Check cancel() when no thread waits on get().",
                          "Check cancel() when thead is blocked on get().",
                          "Check cancel() when promise alread done."]
