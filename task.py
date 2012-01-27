"""
This module contains class Task. It defines methods that are common for all tasks and languages.
"""
from abc import ABCMeta
import os
from tools.executer import execute_process
from tools.checker import checker_ignore_whitespace
from tools.preparator import clean_playground

class Task(metaclass = ABCMeta):
  """
  Abstract class Task. It's used to store task and provides some common functions for all laguages.
  If the language is compilable you should overload method compile.
  """
  path = "./playground/"

  def __init__(self, source, task_id):
    self.source = source
    self.task_id = task_id
  
  def compile(self):
    """                                                        
    This method should be overloaded if language is compilable. It should return None (or thing that
    can be considered as None) if everything was fine and information about error in other case
    """
    return None
  
  def create_files(self):
    source_file = open("{0}{1}".format(self.path, self.filename), "w")
    print(self.source, file = source_file, end = "")
    source_file.close()
  
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
    self.checker = checker_ignore_whitespace
  
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
  from languages.python import PythonTask
  python = PythonTask('print("Hello, world!")', "PYTHON.0");
  python.execute()