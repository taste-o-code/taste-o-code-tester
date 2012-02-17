from __future__ import print_function
from tools.testing_exceptions import *
from tools.preparator import *

class Executor:
  def __init__(self, language, task_id, sources, path):
    self.task = get_task(language, task_id)
    self.path = path
    self.task.sources = sources
    
  def execute(self):
    task = self.task
    path = self.path
    try:
      clean_directory(path)
      self.task.create_files(path)
      task.compile(path)
      task.test(path)
    except CompilationError as exception:
      return ("failed", "Compilation error: " + unicode(exception))
    except Crash as exception:
      return ("failed", "Crash: " + unicode(exception))
    except TimeLimitExceeded as exception:
      return ("failed", unicode(exception))
    except WrongAnswer as exception:
      return ("failed", "Wrong Answer: " + unicode(exception))
    except TesterFailed as exception:
      return ("failed", "Out tester failed on: " + unicode(exception))
    else:
      return ("accepted", None)

if __name__ == "__main__":
  path = "./playground/"
  executor = Executor("CPP", "0", ["""#include <stdio.h>
int main() {
  puts("Hello, world.");
  return 0;
}
"""], path)
  print(executor.execute())

  executor = Executor("CPP", "0", ["""#include <stdio.h>
int main() {
  printf("Hello, world!%c", -1);
  return 0;
}
"""], path)
  print(executor.execute())
  
  executor = Executor("CPP", "0", ["""#include <stdio.hoho>
int main() {
  printf("Hello, world!%c", -1);
  return 0;
}
"""], path)
  print(executor.execute())

  executor = Executor("CPP", "0", ["""#include <stdio.h>
int main() {
  puts("Hello, world.");
  return 1;
}
"""], path)
  print(executor.execute())

  executor = Executor("CPP", "0", ["""#include <stdio.h>
int main() {
  int ololo = 0;
  while (1) {
    ++ololo;
  }
  return 0;
}
"""], path)
  print(executor.execute())

  executor = Executor("PYTHON", "0", ["print('Hello, World!')"], path)
  print(executor.execute())
