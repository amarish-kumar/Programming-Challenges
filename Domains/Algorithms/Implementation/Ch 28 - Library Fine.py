#!/bin/python3

import sys

def calcFee (d1, m1, y1, d2, m2, y2):
    # Returned year(s) after due date
    if (y1 > y2):
        return (10000)
    # Returned year(s) before due date; must be on time
    elif (y1 < y2):
        return (0)
    
    # Returned month(s) after due date
    if (m1 > m2):
        return (500 * (m1 - m2))
    # Returned month(s) before due date; must be on time
    elif (m1 < m2):
        return (0)
    
    # Returned day(s) after due date
    if (d1 > d2):
        return (15 * (d1 - d2))
    
    # Returned on time
    return (0)

d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

print ("%d" % calcFee (d1, m1, y1, d2, m2, y2))
