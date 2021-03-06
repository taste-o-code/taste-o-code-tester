"""Author: Andrey Malevich
This module contains different fucntions which are used to create files that
are necessary to test task (i.e. source files, input files, etc.).
"""
from __future__ import print_function
import os
import testing_exceptions
import codecs
import shutil

def default_file_creator(task, path):
  """Create files for given task.

  This is default function for creating files. It creates file with standart
  name using for language that is used for this task.
  
  Args:
    task: An instance of task class.
    path: Path were files should be created.
  
  Raises:
    WrongSourcesError: Class task is in wrong condition. Sizes of sources,
    postcode and precode are unequal.
  """

  sources = [task.source]
  if (len(task.filenames) != len(sources) or len(task.filenames) != len(task.precode)
      or len(task.filenames) != len(task.postcode)):
    raise testing_exceptions.WrongSourcesError
  for filename, source, precode, postcode in zip(task.filenames, sources, task.precode,
      task.postcode):
    source_file = codecs.open(os.path.join(path, filename), mode='w', encoding='utf-8')
    print(precode + source + postcode, file = source_file, end = "")
    source_file.close()

def create_solution_and_copy_checker(task, path):
  """
  Creates file with user solution in given folder and copies checker from task directory to given folder.
  """
  filename = task.filename
  source_file = codecs.open(os.path.join(path, filename), mode="w", encoding="utf-8")
  print(task.source, file = source_file, end = "")
  source_file.close()
  checker_path = os.path.join(task.directory, task.checker_file)
  shutil.copy(checker_path, path)

