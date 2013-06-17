from languages.java import JavaTask
from tools.file_creators import create_solution_and_copy_checker
import os, shutil


# Description
# Implement class parser for printing info about .class file.

class MysteryOfClassFileTask(JavaTask):

    def before_test(self, test_dir, test_number):
        data_file = os.path.join(task.directory, '%02d.class' % (test_number - 1))
        shutil.copy(data_file, os.path.join(test_dir, 'inputClass.class'))


task = MysteryOfClassFileTask()
task.set_solution_class_name("ClassParser")
