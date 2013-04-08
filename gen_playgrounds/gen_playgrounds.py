#!/usr/bin/env python2.7
# Run this script under sudo
from __future__ import print_function
from subprocess import check_call
from sys import stdin, exit
import argparse
import shutil
import os
from sh import chmod

APPARMOR_INIT = '/etc/init.d/apparmor'
APPARMOR_PROFILES = '/etc/apparmor.d/'

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = "Generates playground and makes apparmor use it")
  parser.add_argument("path")
  args = parser.parse_args()
  path = args.path
  if path[-1] != '/':
    path += '/'

  if os.path.isdir(path):
    # OMG! Careful with it!
    print("This will remove *everything* under " + path + ", are you sure? (y/n)")
    answer = stdin.readline().strip()
    if answer != 'y' and answer != 'yes':
      print("Then provide another path, bye")
      exit(0)
    shutil.rmtree(path)

  os.mkdir(path)

  files_path = os.path.join(path, 'files')
  os.mkdir(files_path)
  for executable in open('copy-executables'):
    executable = executable.strip()
    if executable == '': continue
    shutil.copy(executable, files_path)

  playground_with_subdir = os.path.join(path, '**') # all subdirectories and files
  profile = open('profile').read().format(playground_with_subdir, playground_with_subdir)
  output = open(os.path.join(APPARMOR_PROFILES, playground_with_subdir.replace('/','.')[1:]), 'w')
  print(profile, file = output)
  output.close()

  # Copy java policy
  java_policy = open('java.policy').read().format(path)
  policy_file = open(os.path.join(files_path, 'java.policy'), 'w')
  print(java_policy, file = policy_file)
  policy_file.close()

  check_call([APPARMOR_INIT, 'restart'])
  chmod('777', path)

