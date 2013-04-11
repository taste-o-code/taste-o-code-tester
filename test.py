from executor import Executor

lang = 'UNLAMBDA'
task = 'hello-world'
solution = open('solutions/' + lang + '/' + task + '.unl').read()
result = Executor(lang, task, solution, '/home/playground/1/').execute()

print result
