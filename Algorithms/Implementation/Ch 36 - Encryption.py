#!/bin/python3

import sys
import math

def printIt (r, c, length):
    tBuffer = ""
    
    # Iterate through each printing column
    for j in range (0, c, 1):
        t = ""
        pos = 0
        
        # Iterate through each row's jth value
        for i in range (0, r, 1):
            if (j + pos >= length):
                continue
            else:
                t += (s[j + pos])
            
            pos += c
        
        tBuffer += t + " "
    print ("%s" % tBuffer)

def findBestFactors (length):
    i = 0
    j = 0
    minimum = math.floor (math.sqrt (length))
    maximum = math.ceil (math.sqrt (length))
    
    # If the square is nice, we have found the only answer
    if (maximum == minimum):
        return (minimum, maximum)
    
    # If the square is ugly, we have 3 options
    
    # If lowest possible multiplication works, use it
    if (minimum * minimum >= length):
        return (minimum, minimum)
    
    # Try this one
    if (minimum * maximum >= length):
        return (minimum, maximum)
    
    # If that didn't work, we gotta use this
    return (maximum, maximum)

s = input().strip()

length = len (s)

r, c = findBestFactors (length)
printIt (r, c, length)
