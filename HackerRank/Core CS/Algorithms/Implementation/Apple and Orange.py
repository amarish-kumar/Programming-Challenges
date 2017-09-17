# Python 3.x

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

total_apple = 0
total_orange = 0

for val in apple:
    if val > 0: # Apples have fallen to the right of the apple tree
        if val + a >= s and val + a <= t: #Apples fell on the house
            total_apple += 1

for val in orange:
    if val < 0: # Oranges have fallen to the left of the orange tree
        if val + b >=s and val + b <= t:
            total_orange += 1

print ("%d\n%d" % (total_apple, total_orange))
