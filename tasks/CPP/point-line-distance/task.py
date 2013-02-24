from languages.cpp import CppTaskWithChecker
from tools.checkers import checker_floats

# Write function 'distance' that calculates distance from point to a line.
task = CppTaskWithChecker()
task.checker = checker_floats
