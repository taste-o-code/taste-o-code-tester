from languages.java import JavaTask

# Description
# Implement DI container.

task = JavaTask()
task.set_solution_class_name("DependencyInjector")
task.test_descriptions = ["Checks getComponent(Class).",
                          "Checks getComponent(String).",
                          "Checks classes registration in inverse order: injected component registered last.",
                          "Checks that null injected when no components match.",
                          "Checks that null is returned when not registered component is requested.",
                          "Checks Scope.SINGLETON",
                          "Checks Scope.PROTOTYPE",
                          "Checks inheritance: super class fields must be also processed by container."]
