#include <vector>
#include <iostream>

using namespace std;

int main(){
    int n;  // Rows of matrix to follow with N numbers each
    
    cin >> n;
    
    vector<vector <int>> a (n, vector <int> (n)); // Matix vector
    int sum, sumInv = 0; // Sum of left-right and right-left diagonals
    
    // Go through the matrix and sum the diagonals
    for (int a_i = 0; a_i < n; a_i++){
       for (int a_j = 0; a_j < n; a_j++){
          cin >> a[a_i][a_j];
           
           if (a_i == a_j) {
               sum += a[a_i][a_j];
           }
           if (a_j == ((n - 1) - a_i)) {
               sumInv += a[a_i][a_j];
           }
       }
    }
    
    // Find the difference
    sum = sum - sumInv;
    
    // Get the absolute value of diff
    if (sum < 0) {
        sum *= -1;
    }
    
    // Print out the difference
    cout << sum;
    
    return 0;
}
