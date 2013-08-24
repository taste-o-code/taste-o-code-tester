from languages.java import JavaTask

# Description
# Implement gesture recognition algorithm. It takes 2-d array of points (each row - array of points at particular moment).
# should recogninze slide left/right/up/down, double slide left/right/up/down and zoom in/out gestures.

task = JavaTask()
task.set_solution_class_name("GestureRecognition")
task.test_descriptions = ["Slide right.",
                          "Slide right.",
                          "Slide left.",
                          "Slide left.",
                          "Slide up.",
                          "Slide up.",
                          "Slide down.",
                          "Slide down.",
                          "Double slide right",
                          "Double slide right",
                          "Double slide left",
                          "Double slide left",
                          "Double slide up",
                          "Double slide up",
                          "Double slide down",
                          "Double slide down",
                          "Zoom in (horizontal)",
                          "Zoom in (vertical)",
                          "Zoom out (horizontal)",
                          "Zoom out (vertical)"]
