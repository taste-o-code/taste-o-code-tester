from executor import Executor

lang = 'CPP'
task = 'matrix-mult'
solution = open('tasks/' + lang + '/' + task + '/solution/solution.cpp').read()
result = Executor(lang, task, solution, '/home/playground/1/').execute()

print result
