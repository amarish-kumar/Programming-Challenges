#!/bin/python3

import sys

n = int(input().strip())

binary = list (bin (n) [2::])

biggest = 0
current = 0

for i in range (0, len (binary), 1):
    if (binary [i] != '1'):
        current = 0
    else:
        current += 1
    
        if (current > biggest):
            biggest = current
        
print ("%d" % biggest)
