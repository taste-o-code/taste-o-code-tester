from __future__ import print_function
from tester_exceptions import *
from tools.preparator import *

class Executor:
  path = "./playground/"
  def __init__(self, task_id, sources):
    self.task = get_task(task_id)
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
      print("Compilation error:" + str(exception))
    except Crash as exception:
      print("Crash:" + str(exception))
    except WrongAnswer as exception:
      print("Wrong Answer: " + str(exception));
    else:
      print("AC")

if __name__ == "__main__":
  executor = Executor("CPP.0", ["""#include <stdio.h>
int main() {
  puts("Hello, world.");
  return 0;
}
"""])
  executor.execute()
  
  executor = Executor("CPP.0", ["""#include <stdio.hoho>
int main() {
  puts("Hello, world!");
  return 0;
}
"""])
  executor.execute()

  executor = Executor("CPP.0", ["""#include <stdio.h>
int main() {
  puts("Hello, world.");
  return 1;
}
"""])
  executor.execute()

  executor = Executor("PYTHON.0", ["print('Hello, World!')"])
  executor.execute()
