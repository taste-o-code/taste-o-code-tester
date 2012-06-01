from languages.cpp import CppTask

task = CppTask()
task.compile_string = "g++ {0}main.cpp -o {0}main.out -O2 --openmp"

