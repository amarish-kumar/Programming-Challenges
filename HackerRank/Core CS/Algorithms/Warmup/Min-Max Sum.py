#Python 3.x

import sys

vals = list (map (int, input().strip().split(' ')))

min_sum = 0
max_sum = 0

for i in range (0, 5, 1):
    e_vals = list (vals)
    del e_vals [i]
    curr_sum = sum (e_vals)

    if (curr_sum > max_sum):
        max_sum = curr_sum

    if (min_sum == 0):
        min_sum = curr_sum
    elif (curr_sum < min_sum):
        min_sum = curr_sum

print ("%d %d" % (min_sum, max_sum))
