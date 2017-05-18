#!/bin/python3

import sys

def findPairs (init):
    tvp = 0
    
    for i in range (n - 1, init, -1):
        #print ("(%d, %d) -> (%d + %d) mod %d = %d" % (init, i, a[init], a[i], k,  (a[init] + a[i]) % k))
        if (a[init] + a[i]) % k == 0:
            tvp += 1
    
    return (tvp)

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

vp = 0

for i in range (0, n, 1):
    vp += findPairs (i)

print ("%d" % vp)
