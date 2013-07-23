from executor import Executor

lang = 'CLOJURE'
task = 'missing-coordinates'
solution = open('solutions/' + lang + '/' + task + '.clj').read()
result = Executor(lang, task, solution, '/home/playground/1/').execute()

print result
