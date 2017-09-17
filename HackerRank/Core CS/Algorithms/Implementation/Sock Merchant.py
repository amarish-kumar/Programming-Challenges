# Python 3.5

import sys
from collections import Counter

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

z = Counter (c)
total_socks = 0

for (val, occ) in z.most_common ():
    if (occ % 2 == 0): # Cleanly pairable
        total_socks += occ / 2
    elif ((occ - 1) > 0): # Odd contains pairables
        total_socks += (occ - 1) / 2

print ("%d" % total_socks)
