class WrongSourcesError(BaseException):
  pass

class WrongAnswer(BaseException):
  pass

class TimeLimitExceeded(BaseException):
  def __init__(self, test_number):
   self = BaseException.__init__(self, "Code execution time limit exceeded on test #%s" % test_number)

class CompilationError(BaseException):
  pass

class CompilationLimitExceeded(CompilationError):
  def __init__(self):
   self = BaseException.__init__(self, "Compilation time limit exceeded")

class Crash(BaseException):
  pass

class TesterFailed(BaseException): 
  pass
