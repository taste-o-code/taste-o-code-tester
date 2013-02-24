from math import isnan

"""Author: Andrey Malevich
This module contains different checkers which are used to test outputs of
programs.
"""

def get_tokens(text):
  """Splits output into tokens.

  This function is used to split text into tokens that need to be compared.

  Args:
    text: Text to be splited into tokens.

  Returns:
    Function returns a list of tokens.
  """
  return text.split()

def checker_naive(correct, output):
  """Checks corrent and output be equal in every symbol.

  This function is used to compare user output and correct answer to be equal
  in every symbol.

  Args:
    correct: Expected output of program.
    output: What program has returned.

  Returns:
    True if correct and output are equal, and False otherwise.
  """
  return correct == output

def checker_ignore_whitespace(correct, output):
  """Checks corrent and output be equal ignoring all whitespace symbols.

  This function is used to compare user output and correct answer to be equal
  in every non whitespace symbol.

  Args:
    correct: Expected output of program.
    output: What program has returned.

  Returns:
    True if correct and output are equal, and False otherwise.
  """
  return get_tokens(correct) == get_tokens(output)

def checker_floats(correct, output, eps = 1e-6):
  """Checks corrent and output be equal ignoring all whitespace symbols and
  checking all float numbers to differ in no more than eps.

  This function is used to compare user output and correct answer to be equal
  ignoring all whitespace and assuming floats to be equal if they differ in no
  more than eps.

  Args:
    correct: Expected output of program.
    output: What program has returned.

  Returns:
    True if correct and output are equal, and False otherwise.
  """
  correct = get_tokens(correct)
  output = get_tokens(output)
  if (len(correct) != len(output)):
    return False
  for (first, second) in zip(correct, output):
    if first == second:  #If values are equal (floats or strings, or smth else)
      continue
    try: #Otherwise we assume that they are floats
      first = float(first)
      second = float(second)
      if isnan(first) or isnan(second):
        return False
      if first > second + eps or second > first + eps:  #In case they differ in
          # more than eps
        return False
    except ValueError as e: #In case if one them is not float then we got WA.
      return False
  return True
