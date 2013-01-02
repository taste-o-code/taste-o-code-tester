from os.path import join
import unittest, config, os
import executor
import logging

PLAYGROUND_TEST_DIR = os.path.join(config.PLAYGROUND_PATH, 'test')

logging.basicConfig(level = logging.DEBUG)

class LanguageTester(unittest.TestCase):


    def task_solution(self, language, task):
        solution_dir = join(config.TASKS_PATH, language, task, 'solution')
        files = os.listdir(solution_dir)
        self.assertEqual(len(files), 1, msg = 'Only 1 solution expected for each task now.')
        return open(join(solution_dir, files[0])).read()

    def run_task(self, language, task):
        logging.info('Testing %s %s' % (language, task))
        source = self.task_solution(language, task)
        result = executor.Executor(language, task, source, PLAYGROUND_TEST_DIR).execute()
        self.assertEqual(result[0], 'accepted', msg = ("Task %s %s doesn't pass. Result: %s" % (language, task, result)))


    def run_all_tasks(self, language):
        language_dir = join(config.TASKS_PATH, language)
        for task in os.listdir(language_dir):
            task_dir = join(language_dir, task)
            if os.path.isdir(task_dir):
                self.run_task(language, task)



class UnlambdaTest(LanguageTester):

    def test(self):
        self.run_all_tasks('UNLAMBDA')



class ClojureTest(LanguageTester):

    def test(self):
        self.run_all_tasks('CLOJURE')


class PrologTest(LanguageTester):

    def test(self):
        self.run_all_tasks('PROLOG')


class CppTest(LanguageTester):

    def test(self):
        self.run_all_tasks('CPP')

class JavaTest(LanguageTester):

    def test(self):
        self.run_all_tasks('JAVA')
