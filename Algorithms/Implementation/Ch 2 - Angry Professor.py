#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]

    rn = 0
    # Check to make sure there are enough students
    if n < k:
        print ("YES")
        continue
    
    # Iterate through the student arrival times
    for i_t in a:
        # If they are on time, mark them as real
        if i_t <= 0:
            rn += 1
   
    # Compare real students to theoretical students
    #  If the number is >= the threshold, we are good
    if rn >= k:
        print ("NO")
    else:
        print ("YES")
