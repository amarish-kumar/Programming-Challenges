using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        double mealCost;    // The base cost of the meal
        int tipPercent;     // The integer percentage of tip required
        int taxPercent;     // The integer percentage of tax required
        
        mealCost = Convert.ToDouble(Console.ReadLine ());
        tipPercent = Convert.ToInt16 (Console.ReadLine ());
        taxPercent = Convert.ToInt16 (Console.ReadLine ());
        
        Console.WriteLine ("The total meal cost is {0} dollars.", Math.Round (mealCost + 
                                                                              (mealCost * tipPercent / 100) + 
                                                                              (mealCost * taxPercent / 100)));
    }
}
