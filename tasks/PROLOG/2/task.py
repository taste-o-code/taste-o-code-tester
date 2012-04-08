from languages.prolog import PrologTask
import os

# Description
# Write predicate path(Parent, Child, Path), given predicates parent/2

def tree_database():
    dirname = os.path.dirname(os.path.abspath(__file__))
    family = open(os.path.join(dirname, 'tree.pl'), 'r')
    return family.read()

class PrologTreeTask(PrologTask):
    precode = [tree_database()]

task = PrologTreeTask()
