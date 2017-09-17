# Python 3.5

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # Create int list
    n_l = list (map (int, list (str(n))))

    # Number of valid divisions
    num_valid = 0

    #Interate through the number
    for num in n_l:
        # Check of 0
        if (num == 0):
            continue
        elif (n % num == 0):
            num_valid += 1

    print (num_valid)
