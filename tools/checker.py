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

def checker_doubles(correct, output, eps = 1e-6):
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
      if first > second + eps or second > first + eps: #In case they are differ in more than eps
        return False
    except ValueError as e: #In case if one them is not float then we got WA/
      return False
  return True
  
if __name__ == '__main__':
  correct  = "Ololo I love spam";
  output = "Ololo       I love\r\nspam                       "
  print(checker_naive(correct, output))
  print(checker_ignore_whitespace(correct, output))
  
  correct = "0.9999991 or 0.5   "
  output = "1 or    \n 0.4999999999"
  print(checker_doubles(correct, output))
  output = "1 or 0.5  1"
  print(checker_doubles(correct, output))
  output = "1 a 0.5"
  print(checker_doubles(correct, output))
  output = "1 or a0.5"
  print(checker_doubles(correct, output))
