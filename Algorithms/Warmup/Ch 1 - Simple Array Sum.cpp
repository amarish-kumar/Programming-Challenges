#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n;        // Number of elements
    int sum = 0;  // The sum of values in array
    
    // Get number of elements
    cin >> n;
    // Create the array
    vector<int> arr(n);
    
    // Go through array and sum all values
    for(int i = 0; i < n; i++){
        // Read character of index i on line
        cin >> arr[i];
        // Add it
        sum += arr[i];
    }
    
    // Print the sum to the console
    cout << sum;
    
    return (0);
}
