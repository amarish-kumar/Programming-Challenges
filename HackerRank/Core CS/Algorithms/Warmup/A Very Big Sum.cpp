#include <vector>
#include <iostream>

using namespace std;


int main(){
    int n;  // Number of integers to follow
    
    cin >> n;
    
    vector<int> arr(n); // Vector of integers
    long long sum = 0;  // Sum of the integers in arr
    
    // Go through vector and add each value to sum
    for(int arr_i = 0; arr_i < n; arr_i++){
        // Get next vector item
        cin >> arr[arr_i];
        // Add it to sum
        sum += arr[arr_i];
    }
    
    cout << sum;
    
    return 0;
}
