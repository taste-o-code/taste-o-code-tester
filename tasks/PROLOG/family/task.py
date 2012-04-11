from languages.prolog import PrologTask
import os

# Description
# Write predicates father/2, mother/2, sister/2, brother/2, given predicates male/1, female/1, parent/2

def family_database():
    dirname = os.path.dirname(os.path.abspath(__file__))
    family = open(os.path.join(dirname, 'family.pl'), 'r')
    return family.read()

class PrologFamilyTask(PrologTask):
    precode = [family_database()]

task = PrologFamilyTask()
