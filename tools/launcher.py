""" Author: Malevich Andrey
This module contains a set of functions that are used for executing system
calls such as compling, running, etc.
"""
from __future__ import print_function
from subprocess import CalledProcessError
#from tester_exceptions import TesterFailed
import subprocess
import sys
import logging
import shlex


def execute_process(command, input = "", timelimit = 3, testdir = None):
  """Executes process.
  
  This function should be used for executing all system calls on server whose
  execution is independent from process output. It also limit's exection time.
  
  Args:
    testdir: path to a current testing directory
    command: System call that should be executed.
    input: String that should be given to command as input.
    timelimit: Limit of time that is given to execute program.
  
  Returns:
    Function returns a tuple consisting of return code, stdout, stderr.
  
  Raises:
    TesterFailed: There were problems with encoding test data.
  """
  encoding = sys.getfilesystemencoding() #Using system encoding for all strings.
  try:
    if sys.platform == 'win32':
      #Local testing
      pass
    else:
      #Onsite testing
      command = "timeout " + str(timelimit) + " " + command;

    process = subprocess.Popen(shlex.split(command), stdin = subprocess.PIPE,
    stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd = testdir)
    #Write input to stdin and read stdout, stderr to EOF and waits until process
    #terminate.
    stdout, stderr = process.communicate(input)
    exitcode = process.returncode
    return (exitcode, stdout.decode(encoding), stderr.decode(encoding))
  except CalledProcessError as e: #In case if called process crashed
    return (e.errno, "", str(e));
  except UnicodeEncodeError as e: #Something went wrong with encoding result
    print("Failed. There problems with encoding " + input, file = sys.stderr)
    raise TesterFailed("Failed on command " + command)
  except UnicodeDecodeError as e: #Something went wrong with decoding result
    return (exitcode, "", str(e));
