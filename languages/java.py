"""
This module contains class to test Java solutions
"""
import compilableTask

class JavaTask(compilableTask.CompilableTask):
  """
  This class contains overloads of functions used specialy for testing Java tasks
  """
  compile_string = "javac {0}Main.java"
  execute_string = "java {0}Main"
  filename = ["Main.java"]
