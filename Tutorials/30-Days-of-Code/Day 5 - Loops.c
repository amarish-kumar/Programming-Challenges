#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int N; 
    scanf("%d",&N);
    
    char* outputBuffer = malloc (sizeof (char) * 14 * 10);
    char* sBuffer = malloc (sizeof (char) * 15);
    
    for (int i = 1; i < 11; i++) {
        sprintf (sBuffer, "%d x %d = %d\n", N, i, N * i);
        strcat (outputBuffer, sBuffer);
    }
    
    printf ("%s", outputBuffer);
    return 0;
}
