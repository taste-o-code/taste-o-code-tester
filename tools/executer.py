"""
This module contains a set of functions that are used for executing system calls
such as compling, running
"""
import subprocess, sys

def execute_process(command, input = "", timelimit = 3):
  """
  This function should be used for executing all system calls on server. It limits
  exection time. (Other restrictions can be added)
  """
  try:
    if sys.platform == 'win32':
      #Local testing
      pass
    else:
      #Onsite testing
      command = "timeout " + str(timelimit) + " " + command;
    process = subprocess.Popen(command.split(), stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    process.stdin.write(input.encode("UTF-8"))
    process.stdin.flush()
    process.stdin.close()
    process.wait()
    return process.stdout.read().decode("UTF-8")
     
  except subprocess.CalledProcessError as e:
    return "Process failed with executing:\n%s" % e;
