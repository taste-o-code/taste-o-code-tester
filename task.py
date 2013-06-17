"""
This module contains class Task. It defines methods that are common for all tasks and languages.
"""
from abc import ABCMeta
import os
from tools.checkers import checker_ignore_whitespace
from tools.compilers import *
from tools.file_creators import *
from tools.preparator import *
from tools.testers import *

class Task(object):
  """
  Class Task. It's used to store task and provides some common functions for all laguages.
  If the language is compilable you should overload method compile.
  """
  precode = [""]
  postcode = [""]

  def __init__(self, create_files = default_file_creator, tester = default_tester,
      checker = checker_ignore_whitespace):
    self.create_files = create_files.__get__(self)
    self.test = tester.__get__(self)
    self.checker = checker


  """
  Compiles a task
  Overload this method if language is compilable.

  Raises:
    CompilationError
  """
  def compile(self, path):
    pass

  """
  Runs before each task.
  Can be used to copy necessary per-test files.
  """
  def before_test(self, test_dir, test_number):
    pass

