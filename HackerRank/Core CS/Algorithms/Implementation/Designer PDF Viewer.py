# Python 3.5

import sys
import string
import itertools

h = [int(h_temp) for h_temp in input().strip().split(' ')]

heights = dict (zip (string.ascii_lowercase, itertools.cycle (h)))
word = list (input().strip())

width = 1

total_width = len (word) * width
total_height = 0

for letter in word:
    new_height = heights [letter]

    if (new_height > total_height):
        total_height = new_height

print ("%d" % (total_width * total_height))
