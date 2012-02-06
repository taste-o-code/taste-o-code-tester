""" Author: Malevich Andrey
This module contains a set of functions that are used to prepare execution of
task.
"""

import os
from os.path import join
from importlib import import_module

def get_task(task_id):
  """Gets task.
  
  This function is used to get a Task which is going to be tested.
  
  Args:
    task_id: Id of task which we are going to test.
  
  Returns:
    Task that will be used for testing solution/
  """
  language, id = task_id.split('.')
  task_module = import_module("tasks." + task_id + ".task")
  task = task_module.task
  path = join(".", "tasks", language, id)
  task.tests = [(open(join(path, x), "r").read(),
      open(join(path, x[:-2] + "out"), "r").read())
    for x in filter(lambda x: x.endswith(".in"), os.listdir(path))]
  return task

def clean_directory(path):
  """Cleans testing area.
  
  This function is used to clean testing area from all files from previous
  solutions.
  
  Args:
    path: Path to testing area.
  """
  for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
      os.unlink(file_path)
