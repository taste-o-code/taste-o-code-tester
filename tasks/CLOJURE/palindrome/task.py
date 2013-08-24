from languages.clojure import ClojureEvalTask

# Description
# Write function palindrome? to determine whether passed sequence palindrome or not

task = ClojureEvalTask()

task.test_descriptions = ["Checks collection of single element.",
                          "Checks collection.",
                          "Checks collection that contains other collections.",
                          "Checks collection.",
                          "Checks collection of keywords.",
                          "Checks string.",
                          "Checks string.",
                          "Checks string."]
