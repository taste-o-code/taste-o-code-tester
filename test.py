from executor import Executor

lang = 'JAVA'
task = 'mystery-of-class-file'
solution = open('solutions/' + lang + '/' + task + '.java').read()
result = Executor(lang, task, solution, '/home/playground/1/').execute()

print result
