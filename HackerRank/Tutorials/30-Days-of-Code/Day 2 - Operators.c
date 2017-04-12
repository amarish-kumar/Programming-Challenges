#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    double mealCost;    // The base cost of the meal
    int tipPercent;     // The integer percentage of tip required
    int taxPercent;     // The integer percentage of tax required
    
    scanf ("%lf\n%d\n%d", &mealCost, &tipPercent, &taxPercent);
    
    printf ("The total meal cost is %d dollars.", (int) round (mealCost + 
                                                               (mealCost * tipPercent / 100) + 
                                                               (mealCost * taxPercent / 100)));
    return 0;
}
