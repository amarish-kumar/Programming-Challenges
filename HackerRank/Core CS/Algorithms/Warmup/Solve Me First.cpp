#include <iostream>

using namespace std;

// Addition function
int solveMeFirst(int a, int b) {
    return (a + b);
}

int main() {
  int num1, num2; // Integers to be added
  int sum;        // Sum of the addition
  
  // Get two numbers from the user
  cin >> num1 >> num2;
  
  // Process sum
  sum = solveMeFirst(num1,num2);
  
  // Print sum to the console
  cout << sum;
  
  return (0);
}
