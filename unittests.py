import unittest
from tools.checkers import *

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

    

if __name__ == "__main__":
  unittest.main()

