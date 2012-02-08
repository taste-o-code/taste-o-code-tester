""" Author: Malevich Andrey
This module contains a set of functions that are used for executing system
calls such as compling, running, etc.
"""
from subprocess import CalledProcessError
import subprocess
import sys


def execute_process(command, input = "", timelimit = 3):
  """Executes process.
  
  This function should be used for executing all system calls on server whose
  execution is independent from process output. It also limit's exection time.
  
  Args:
    command: System call that should be executed.
    input: String that should be given to command as input.
    timelimit: Limit of time that is given to execute program.
  
  Returns:
    Function returns a tuple consisting of return code, stdout, stderr.
  """
  encoding = sys.getfilesystemencoding() #Using system encoding for all strings.
  try:
    if sys.platform == 'win32':
      #Local testing
      pass
    else:
      #Onsite testing
      command = "timeout " + str(timelimit) + " " + command;
    process = subprocess.Popen(command.split(), stdin = subprocess.PIPE,
      stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    process.stdin.write(input.encode(encoding))
    process.stdin.flush()
    process.stdin.close()
    exitcode = process.wait() #wait returns exitcode of proccess
    return (exitcode, process.stdout.read().decode(encoding),
      process.stderr.read().decode(encoding))
  except CalledProcessError as e: #In case if called process crashed
    return (e.errno, "", str(e));
  except UnicodeEncodeError as e: #Something went wrong with decoding result
    return (e.errno, "", str(e));
