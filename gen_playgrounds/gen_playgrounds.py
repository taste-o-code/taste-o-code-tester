#!/usr/bin/env python2.7
from subprocess import check_call
from sys import stdin, exit
import argparse
import shutil
import os
import __future__ print_function

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = "Generates several playgrounds and makes apparmor use them")
  parser.add_argument("path")
  parser.add_argument("--count", default=4, type=int)
  args = parser.parse_args()
  path = args.path

  if os.path.isdir(path):
    # OMG! Careful with it!
    print("This will remove *everything* under " + path + ", are you sure? (y/n)")
    answer = stdin.readline().strip()
    if answer != 'y' and answer != 'yes':
      print("Then provide another path, bye")
      exit(0)
    shutil.rmtree(path)

  os.mkdir(path)
  for number in xrange(args.count):
    os.mkdir(os.path.join(path, str(number)))
  
  sandbox_path = os.path.join(path, 'sandbox-executables') 
  os.mkdir(sandbox_path)
  for executable in open('copy-executables'):
    executable = executable.strip()
    if executable == '': continue
    check_call(["cp", executable, sandbox_path])

  profile = open('profile').read().format(os.path.join(path, '**'))

  for entry in os.listdir(sandbox_path):
    output = open(os.path.join("/etc/apparmor.d/", os.path.join(sandbox_path, entry).replace('/', '.')[1:]), 'w')
    #for now, using a single profile for all binary types
    print (profile, file=output, end='')
    #output = open(os.path.join("/etc/apparmor.d/", os.join(sandbox_path, entry).replace('/', '.')))
 
#  output = open("/etc/apparmor.d/



