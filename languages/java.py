"""
This module contains class to test Java solutions
"""
from __future__ import print_function
from compilable_task import CompilableTask
from tools.file_creators import create_solution_and_copy_checker
import os
import codecs
import shutil
import config

class JavaTask(CompilableTask):

  def __init__(self):
    CompilableTask.__init__(self, create_files = create_solution_and_copy_checker)
    self.execute_string = "java -Djava.security.manager -Xmx140m -Djava.security.policy={0}/java.policy -cp {{0}} Checker".format(config.PLAYGROUND_FILES_PATH)
    self.checker_file = "Checker.java"
    self.filename = "Solution.java"
    self.compile_strings = ["javac {0}/Solution.java", "javac -cp {0} {0}/Checker.java"]

  def set_solution_class_name(self, name):
    self.filename = name + ".java"
    self.compile_strings[0] = "javac {0}/" + self.filename
