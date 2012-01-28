"""
This module contains all functions that are needed to prepare playground for running tasks.
"""
import os

def clean_playground(path):
  """
  This function is used to clean playground from all files from previous tasks.
  """
  for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
      os.unlink(file_path)

def create_file(path, filename, content):
  pass

