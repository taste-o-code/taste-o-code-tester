from compilable_task import CompilableTask

def parse_list(result):
    open_brackets = 0
    items = set()
    item = ''
    for ch in result[1:-1].strip():
        if ch == ',' and open_brackets == 0:
            items.add(item.strip())
            item = ''
            continue
        elif ch == '[':
            open_brackets += 1
        elif ch == ']':
            open_brackets -= 1
        item += ch
    if item != '':
        items.add(item.strip())
    return set(items)

def check(expected, real):
    result = real.splitlines().pop()
    return parse_list(result) == parse_list(expected)


class PrologTask(CompilableTask):
    filenames = ['prolog.pl']
    compile_strings = ["gplc {0}/prolog.pl -o {0}/prolog"]
    execute_string = "{0}/prolog"

    def __init__(self):
        CompilableTask.__init__(self, checker = check)



