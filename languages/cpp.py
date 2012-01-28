"""
This module contains class to test C++ solutions
"""
import compilableTask

class CppTask(compilableTask.CompilableTask):
  compile_string = "g++ {0}main.cpp -o {0}main.out"
  execute_string = "{0}main.out"
  filename = "main.cpp"
