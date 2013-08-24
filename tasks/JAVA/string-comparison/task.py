from languages.java import JavaTask

# Description
# Implement method that returns one of 3 different string comparator: ascending, descending, byLength, byWordCount.

task = JavaTask()
task.set_solution_class_name("StringComparison")
task.test_descriptions = ["Checks ascending order.",
                          "Checks descending order.",
                          "Checks by length order."
                          "Checks by word count order."]
