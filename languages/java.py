"""
This module contains class to test Java solutions
"""
from __future__ import print_function
from compilable_task import CompilableTask
import os
import codecs
import shutil

def create_solution_and_copy_checker(task, path):
  """
  Creates file with user solution in given folder and copies java file with checker from task directory to given folder.
  """
  filename = task.filename
  source_file = codecs.open(os.path.join(path, filename), mode='w', encoding='utf-8')
  print(task.source, file = source_file, end = "")
  source_file.close()
  checker_path = os.path.join(task.directory, task.checker_file)
  shutil.copy(checker_path, path)



class JavaTask(CompilableTask):
  compile_strings = ["javac {0}/Solution.java", "javac -cp {0} {0}/Checker.java"]
  execute_string = "java -cp {0} Checker"
  filename = "Solution.java"
  checker_file = "Checker.java"

  def __init__(self):
    CompilableTask.__init__(self)
    self.create_files = create_solution_and_copy_checker.__get__(self)
