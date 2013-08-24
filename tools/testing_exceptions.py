class WrongSourcesError(BaseException):
  pass

class WrongAnswer(BaseException):
  pass

class TimeLimitExceeded(BaseException):
  pass

class CompilationError(BaseException):
  pass

class CompilationLimitExceeded(CompilationError):
  def __init__(self):
   self = BaseException.__init__(self, "Compilation time limit exceeded")

class Crash(BaseException):
  pass

class TesterFailed(BaseException): 
  pass
