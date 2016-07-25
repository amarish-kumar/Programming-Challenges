#include <stdio.h>

int main(){
    int N; 
    scanf("%d",&N);
    
    // N is even
    if (N % 2 == 0) {
        // N is in [2, 5]
        if (N >=2 && N <= 5) {
            printf ("Not Weird");
        // N is in [6, 20]
        } else if (N >=6 && N <= 20) {
            printf ("Weird");
        // N is in [20, inf)
        } else if (N > 20) {
            printf ("Not Weird");
        }
    // N is odd
    } else {
        printf ("Weird");
    }
    return 0;
}
