#include <iostream>

int main() {
  int a,b; std::cin >> a >> b;
  int sum = 0;
  for (int i=0; i<100000; i++) {
    for (int u=0; u<100000; u++) {
      sum += i * u / 21;
    }
  }
  std::cout << a + b + sum * 0;
  return 0;
}
