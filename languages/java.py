"""
This module contains class to test Java solutions
"""
import compilableTask

class JavaTask(compilableTask.CompilableTask):
  compile_string = "javac {0}Main.java"
  execute_string = "java {0}Main"
  filename = "Main.java"
