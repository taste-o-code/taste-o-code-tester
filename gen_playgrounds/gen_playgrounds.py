#!/usr/bin/env python2.7
# Run this script under sudo
from __future__ import print_function
from subprocess import check_call
from sys import stdin, exit
import argparse
import shutil
import os

APPARMOR_INIT = '/etc/init.d/apparmor'
APPARMOR_PROFILES = '/etc/apparmor.d/'

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = "Generates several playgrounds and makes apparmor use them")
  parser.add_argument("path")
  parser.add_argument("--count", type=int, default=4)
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
    shutil.copy(executable, sandbox_path)
#    check_call(["cp", executable, sandbox_path])

  playground_with_subdir = os.path.join(path, '**') # all subdirectories and files
  profile = open('profile').read().format(playground_with_subdir, playground_with_subdir)

  for entry in os.listdir(sandbox_path):
    output = open(os.path.join(APPARMOR_PROFILES, os.path.join(sandbox_path, entry).replace('/', '.')[1:]), 'w')
    #for now, using a single profile for all binary types
    print (profile, file=output, end='')
  
  for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
      cpp_binary = os.path.join(path, entry, 'a.out') #TODO: What is a default cpp binary file ?
      output = open(os.path.join(APPARMOR_PROFILES, cpp_binary.replace('/', '.')[1:]), 'w')
      print(profile, file = output)

  check_call([APPARMOR_INIT, 'restart'])
  check_call(["chmod", '777', '-R',  path])
   
