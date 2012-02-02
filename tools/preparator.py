"""
This module contains all functions that are needed to prepare playground for running tasks.
"""
import os
from os.path import join
from importlib import import_module

def get_task(task_id):
  language, id = task_id.split('.')
  task_module = import_module("tasks." + task_id + ".task")
  task = task_module.task
  path = join(".", "tasks", language, id)
  task.tests = [(open(join(path, x), "r").read(), open(join(path, x[:-2] + "out"), "r").read())
    for x in filter(lambda x: x.endswith(".in"), os.listdir(path))]
  return task

def clean_directory(path):
  """
  This function is used to clean playground from all files from previous tasks.
  """
  for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
      os.unlink(file_path)
