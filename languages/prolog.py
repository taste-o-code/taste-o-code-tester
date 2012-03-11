from compilable_task import CompilableTask

import logging

def parse_list(result):
    items = map(lambda(st): st.strip(), result[1:-1].strip().split(','))
    return set(items)

def prolog_checker(expected, real):
    result = real.splitlines().pop()
    logging.warn("Expected %s" % expected)
    logging.warn("Real %s" % result)
    return parse_list(result) == parse_list(expected)


class PrologTask(CompilableTask):
    filenames = ['prolog.pl']
    compile_string = "gplc {0}prolog.pl -o {0}prolog"
    execute_string = "{0}prolog"

    def __init__(self):
        CompilableTask.__init__(self, checker = prolog_checker)



