#!/bin/python3
import sys

def isWeird (N):
    if (N % 2 != 0):
        return ("Weird")
    elif (N > 20 or N < 6):
        return ("Not Weird")
    else:
        return ("Weird")

N = int (input ())

print (isWeird (N))