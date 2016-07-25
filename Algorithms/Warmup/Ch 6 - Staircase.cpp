#include <string>
#include <iostream>

using namespace std;

int main(){
    int n;  // Number of layers
    
    cin >> n;
    
    string buffer;  // Output buffer
    
    // Go through each layer and print the #
    for (int i = 1; i <= n; i++) {
        // Print spaces
        buffer.append (n - i, ' ');
        // Print pounds
        buffer.append (i, '#');
        // Print line
        cout << buffer << endl;
        // Empty buffer
        buffer = "";
    }
    
    return 0;
}
