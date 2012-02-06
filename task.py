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


class Task(metaclass = ABCMeta):
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
  
  def compile(self, path):
    """                                                        
    This method should be overloaded if language is compilable. It should return None (or thing that
    can be considered as None) if everything was fine and information about error in other case
    """
    return None
