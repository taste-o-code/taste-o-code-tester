"""
This module contains class CompilableTask. It overloads methods from class Task
to make it suitable for compilable languages
"""
import task
from tools.executer import execute_process

class CompilableTask(task.Task):
  def compile(self):
    result = execute_process(self.compile_string.format(self.path))
    return result

#Self testing code
if __name__ == '__main__':
  from languages.cpp import CppTask
  from languages.java import JavaTask
  cpp = CppTask("""#include <stdio.h>
int main() {
  puts("Hello, world.");
  return 0;
}""", "CPP.0");
  cpp.execute()
  #java = JavaTask("public class Main {\n  public static void main(String[] args) {\n    System.out.println(\"Hello, world.\");\n  }\n}\n", "JAVA.0");
  #java.execute()