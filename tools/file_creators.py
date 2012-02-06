"""Author: Andrey Malevich
This module contains different fucntions which are used to create files that
are necessary to test task (i.e. source files, input files, etc.).
"""

import os
import exceptions

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
  if (len(task.filenames) != len(task.sources) or len(task.filenames) != len(task.precode)
      or len(task.filenames) != len(task.postcode)):
    raise exceptions.WrongSourcesError
  for filename, precode, source, postcode in zip(task.filenames, task.sources, task.precode,
      task.postcode):
    source_file = open(os.path.join(path, filename), "w")
    print(precode + source + postcode, file = source_file, end = "")
    source_file.close()
