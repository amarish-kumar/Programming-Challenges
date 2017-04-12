#include <vector>
#include <iostream>

using namespace std;


int main(){
    int n;  // Vector size
    
    cin >> n;
    
    vector<int> arr(n);         // n size array
    float pos, neg, zero = 0;   // Fractions of positives negatives, and zeros in the vector
    
    // Go through the vector to find values
    for(int arr_i = 0; arr_i < n; arr_i++){
        
        cin >> arr[arr_i];
        
        if (arr[arr_i] > 0) {
            pos++;
        } else if (arr[arr_i] < 0) {
            neg++;
        } else {
            zero++;
        }
    }
    
    cout << pos / n << "\n" << neg / n << "\n" << zero / n;
    
    return 0;
}
