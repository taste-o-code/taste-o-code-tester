"""
This module contains class CompilableTask. It overloads methods from class Task
to make it suitable for compilable languages
"""
from task import Task
from tools.launcher import execute_process
from tools.checkers import *
from tools.compilers import *
from tools.file_creators import *
from tools.testers import *

class CompilableTask(Task):
  def __init__(self, create_files = default_file_creator, tester = default_tester,
      checker = checker_ignore_whitespace, compiler = default_compiler):
    Task.__init__(self, create_files, tester, checker)
    self.compile = compiler.__get__(self)
