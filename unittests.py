import unittest
from tools.checkers import *
from executor import Executor
import languages.prolog
import os

class CheckerTest(unittest.TestCase):
  """
  This class is used for testing checkers 
  """
  def test_checker_ignore_whitespace(self):
    correct = "this answer is correct"
    output = "this answer is correct"
    self.assertTrue(checker_ignore_whitespace(correct, output))
    output = "   this  answer\tis\n\rcorrect \r   \n"
    self.assertTrue(checker_ignore_whitespace(correct, output))
    output = "   this  answer\tis\n\rwrong \r   \n"
    self.assertFalse(checker_ignore_whitespace(correct, output))
  
  def test_checker_floats(self):
    #Testing simular to ignore_whitespace
    correct = "this answer is correct"
    output = "this answer is correct"
    self.assertTrue(checker_floats(correct, output))
    output = "   this  answer\tis\n\rcorrect \r   \n"
    self.assertTrue(checker_floats(correct, output))
    output = "   this  answer\tis\n\rwrong \r   \n"
    self.assertFalse(checker_floats(correct, output))
    #Cheking with standart EPS
    correct = "0.9999991 or 0.05   "
    output = "1 or    \n 0.04999999999"
    self.assertTrue(checker_floats(correct, output))
    output = "1 or 0.05  1"
    self.assertFalse(checker_floats(correct, output))
    output = "1 a 0.05"
    self.assertFalse(checker_floats(correct, output))
    output = "1 or a0.05"
    self.assertFalse(checker_floats(correct, output))
    output = "1 or 0.4e-1"
    self.assertFalse(checker_floats(correct, output))
    output = "1 or 0.4e-1"
    self.assertTrue(checker_floats(correct, output, eps = 0.01))

class ExecutorTest(unittest.TestCase):
  """
  Class used to test all testing process of a task
  """
  path = './playgrounds/0/'
  def get_task_path(self, language, task_id):
    return './tasks/' + language + '/' + task_id + '/solution';

  def get_sources(self, language, task_id):
    sources = []
    task_path = self.get_task_path(language, task_id)
    for file in os.listdir(task_path): #TODO: make a normal path here
      sources += [open(os.path.join(task_path, file)).read()]
    return sources
      
  def test_cpp_task1(self):
    sources = self.get_sources("CPP", "1")
    executor = Executor("CPP", "1", sources, self.path)
    self.assertTrue(executor.execute()[0] == 'accepted')

  # tests different whitespaces at the end of input, output and source
  def test_cpp_task2(self):
    sources = self.get_sources("CPP", "2")
    executor = Executor("CPP", "2", sources, self.path)
    self.assertTrue(executor.execute()[0] == 'accepted')

  def test_cpp_task4(self):
    sources = self.get_sources("CPP", "3")
    executor = Executor("CPP", "3", sources, self.path)
    result, message = executor.execute()
    self.assertTrue(message.lower().startswith('code execution time limit'))
  
  def test_cpp_task5(self):
    sources = self.get_sources("CPP", "4")
    executor = Executor("CPP", "4", sources, self.path)
    result, message = executor.execute()
    self.assertTrue(message.lower().startswith('wrong answer'))

  def test_cpp_task6(self):
    sources = self.get_sources("CPP", "5")
    executor = Executor("CPP", "5", sources, self.path)
    result, message = executor.execute()
    self.assertTrue(result == 'failed')
    self.assertTrue(message.lower().startswith('compilation time limit')) #OMG put these string in conf too, better localized

  def test_cpp_task7(self):
    sources = self.get_sources("CPP", "6")
    executor = Executor("CPP", "6", sources, self.path)
    result, message = executor.execute()
    self.assertTrue(result == 'failed')
    self.assertTrue(message.lower().startswith('compilation error'))

  def test_cpp_task8(self):
    sources = self.get_sources("CPP", "7")
    executor = Executor("CPP", "7", sources, self.path)
    result, message = executor.execute()
    self.assertTrue(result == 'accepted')


class PrologTest(unittest.TestCase):

  def test_parse_simple_list(self):
    parsed = languages.prolog.parse_list('[ 1, 2,  3,    10   ]')
    for x in ['1', '2', '3', '10']:
      self.assertIn(x, parsed)

  def test_parse_complex_list(self):
    parsed = languages.prolog.parse_list('[1, 2, [3, 4], [5, [6]], 7]')
    for x in ['1', '2', '[3, 4]', '[5, [6]]', '7']:
      self.assertIn(x, parsed)

  def test_checker_equal(self):
    expected = '[1, 2, 3, 4]'
    got = '[3, 2,    4,      1]'

    result = languages.prolog.check(expected, got)

    self.assertTrue(result)

  def test_checker_different(self):
    expected = '[1, 2, 3, 4]'
    got = '[3, 5, 1, 2]'

    result = languages.prolog.check(expected, got)

    self.assertFalse(result)

  def test_checker_complex_equals(self):
    expected = '[[1, 2], [3, 4]]'
    got = '[[3, 4], [1, 2]]'

    result = languages.prolog.check(expected, got)

    self.assertTrue(result)

  def test_checker_complex_different(self):
    expected = '[[1, 4], [3, 2]]'
    got = '[[3, 4], [1, 2]]'

    result = languages.prolog.check(expected, got)

    self.assertFalse(result)

if __name__ == "__main__":
  unittest.main()

