#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

jumps = 0
i = 0
n_a = n - 1

while (i < n_a):
    #print ("%d >= %d" % (i, n))
    #print ("%d >= %d?" % (n_a, i + 2))
    if (n_a >= i + 2):
        #print ("%d == 0?" % (c[i+2]))
        if (c[i + 2] == 0):
            #print ("hop")
            i += 1
    #print ("walk")
    i += 1
    jumps += 1

print ("%d" % jumps)
