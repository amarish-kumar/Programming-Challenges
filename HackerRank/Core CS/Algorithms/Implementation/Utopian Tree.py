# Python 3.5

import sys

t = int(input())

for a0 in range(t):
    n = int(input().strip())
    height = 1
    toggle = 0
    # If toggle is 0, a double op will be done
    # If toggle is 1, a ++ op will be done

    for i in range (n, 0, -1):
        if (toggle == 0):
            height *= 2
            toggle = 1
        elif (toggle == 1):
            height += 1
            toggle = 0

    print (height)
