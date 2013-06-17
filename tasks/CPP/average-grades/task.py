from languages.cpp import CppTaskWithChecker
from tools.checkers import checker_floats
import shutil
import os

# Write method 'averageGrades' that calculates average grades in each group.

class AverageGradeTask(CppTaskWithChecker):

  def before_test(self, test_dir, test_number):
    data_file = os.path.join(task.directory, '%02d.bin' % (test_number - 1))
    shutil.copy(data_file, os.path.join(test_dir, 'data.bin'))

task = AverageGradeTask()
task.checker = checker_floats

