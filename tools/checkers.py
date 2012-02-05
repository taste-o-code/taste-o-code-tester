"""
This module have different checkers to test outputs of programs
"""

def get_tokens(output):
  return output.split()

def checker_naive(correct, output):
  return correct == output

def checker_ignore_whitespace(correct, output):
  """
  This function is used to test two lists of string to be equal. It ignores all whitespace characters.
  """
  return get_tokens(correct) == get_tokens(output)

def checker_floats(correct, output, eps = 1e-6):
  """
  This function is used to test two lists of floats to be equal with absolute error no more than eps.
  It ignores whitespaces and assumes that all not float tokens must be equal.
  """
  correct = get_tokens(correct)
  output = get_tokens(output)
  if (len(correct) != len(output)):
    return False
  for (first, second) in zip(correct, output):
    if first == second: #If values are equal (floats or strings, or smth else).
      continue
    try: #Otherwise we assume that they are floats
      first = float(first)
      second = float(second)
      if first > second + eps or second > first + eps: #In case they differ in more than eps
        return False
    except ValueError as e: #In case if one them is not float then we got WA/
      return False
  return True
