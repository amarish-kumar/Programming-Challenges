#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int d = 0;
    long int ld = 0;
    long long lld = 0;
    char c = 0;
    float f = 0.0;
    double lf = 0.0;
    
    scanf ("%d %ld %lld %c %f %lf", &d, &ld, &lld, &c, &f, &lf);
    
    printf ("%d\n%ld\n%lld\n%c\n%f\n%lf", d, ld, lld, c, f, lf);
    return 0;
}
