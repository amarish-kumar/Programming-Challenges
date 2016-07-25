#!/bin/python3

import sys




t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    total = 0
    
    # Black is cheaper to buy than white
    if (x < y):
        # Add cost of blacks to the total
        total += b * x    

        # Black -> white conversion is cheaper than new whites
        if ((x + z) < y):
            # Add cost of converted whites to total
            total += (x + z) * w
        # Coverting is not worth it
        else:
            # Add cost of whites to total
            total += w * y

    # Whites is cheaper to buy than blacks    
    elif (x > y):
        # Add cost of whites to the total
        total += w * y    

        # If the white -> black conversion is cheaper than new blacks
        if ((y + z) < x):
            # Add cost of converted blacks to total
            total += (y + z) * b
        # Coverting is not worth it
        else:
            total += b * x
            
    # Both cost the same
    else:
        total += (w * y) + (b * x)
            
    print ("%d" % total)
        
