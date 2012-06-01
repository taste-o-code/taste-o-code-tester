import unittest
import languages.prolog


class PrologCheckerTest(unittest.TestCase):

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
