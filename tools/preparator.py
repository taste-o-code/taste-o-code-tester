""" Author: Malevich Andrey
This module contains a set of functions that are used to prepare execution of
task.
"""

import os
import shutil
from os.path import join
from importlib import import_module

def get_task(language, id):
  """Gets task.
  
  This function is used to get a Task which is going to be tested.
  
  Args:
    task_id: Id of task which we are going to test.
  
  Returns:
    Task that will be used for testing solution/
  """
#  language, id = task_id.split('.')
  task_module = import_module("tasks." + language + "." + id + ".task")
  task = task_module.task
  path = join(".", "tasks", language, id)
  task.tests = [(open(join(path, x), "r").read(),
      open(join(path, x[:-2] + "out"), "r").read())
    for x in filter(lambda x: x.endswith(".in"), os.listdir(path))]
  return task

def prepare_directory(path):
  """Creates directory for testing area.
  
  This function is used to prepare testing area for testing solution.
  
  Args:
    path: Path to testing area.
  """
  if (os.path.exists(path)): #If directory wasn't removed in previous run.
    shutil.rmtree(path)
  os.mkdir(path)

def cleanup(path):
  """Cleans path which was used as testing area.
  
  This function is used to clean path after testing.
  
  Args:
    path: Path to testing area.
  """
  if (os.path.exists(path)):
    shutil.rmtree(path)

