class WrongSourcesError(BaseException):
  pass

class WrongAnswer(BaseException):
  pass

class TimeLimitExceeded(BaseException):
  def __init__(self):
   self = BaseException.__init__(self, "Code execution time limit exceeded")

class CompilationError(BaseException):
  pass

class CompilationLimitExceeded(CompilationError):
  def __init__(self):
   self = BaseException.__init__(self, "Compilation time limit exceeded")

class Crash(BaseException):
  pass

class TesterFailed(BaseException): 
  pass
