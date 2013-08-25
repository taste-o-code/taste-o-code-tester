from executor import Executor

lang = 'JAVA'
task = 'di'
solution = open('solutions/' + lang + '/' + task + '.java').read()
result = Executor(lang, task, solution, '/home/playground/1/').execute(False)

print result
