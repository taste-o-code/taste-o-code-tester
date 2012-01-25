"""
This module contains class Task. It defines methods that are common for all tasks and languages.
"""
from abc import ABCMeta, abstractmethod
import os
from tools.executer import execute_process
from tools.checker import checker_naive
from tools.preparator import clean_playground

class Task(metaclass = ABCMeta):
  """
  Abstract class Task. It's used to store task and provides some common functions for all laguages.
  If the language is compilable you should overload method compile.
  """
  path = "playground/"

  def __init__(self, source, task_id):
    self.source = source
    self.task_id = task_id
  
  def compile(self):
    """
    This method should be overloaded if language is compilable
    """
    return None
  
  @abstractmethod
  def create_files(self):
    pass
  
  def test(self):
    """
    This method is called when we trying to test Task on test. By default it simply checks
    task on all tests and compares output with the correct one using self.checker.
    """
    for input, output in self.tests:
      result = execute_process(self.execute_string.format(self.path), input);
      checker = self.checker
      if not checker(output, result):
        return "WA"
  
  def get_task(self):
    language, task = self.task_id.split('.')
    path = "./tasks/" + language + "/" + task + "/";
    self.precode = open(path + "precode.txt", "r").read()
    self.postcode = open(path + "postcode.txt", "r").read()
    self.tests = [(open(path + x, "r").read(), open(path + x[:-2] + "out", "r").read())
      for x in filter(lambda x: x.endswith(".in"), os.listdir(path))]
    #TODO Here should be code for getting checker from task.
    self.checker = checker_naive
  
  def execute(self):
    """
    This method is called when we need to test the task. It calls all other needed method.
    """
    clean_playground(self.path)
    self.get_task()
    self.create_files()
    result = self.compile()
    if result: #Method should return non empty string if something goes wrong
      print("Compilation failed", result) # Return CE / CLE
      return None

    result = self.test()
    if result:
      print("Wrong answer", result) #Return WA / TL
    else:
      print("Well done!") #Return Ok

#Self testing code
if __name__ == '__main__':
  from languages.cpp import CppTask
  from languages.java import JavaTask
  from languages.python import PythonTask
  cpp = CppTask("#include <stdio.h>\n\nint main() {\n  puts(\"Hello, world.\");\n  return 0;\n}", "CPP.0");
  cpp.execute()
  #java = JavaTask("public class Main {\n  public static void main(String[] args) {\n    System.out.println(\"Hello, world.\");\n  }\n}\n", "JAVA.0");
  #java.execute()
  python = PythonTask("print(\"Hello, world.\")\n", "PYTHON.0");
  python.execute()