from executor import Executor

lang = 'CLOJURE'
task = 'reinvent-hiccup'
solution = open('solutions/' + lang + '/' + task + '.clj').read()
result = Executor(lang, task, solution, '/home/playground/1/').execute(False)

print result
