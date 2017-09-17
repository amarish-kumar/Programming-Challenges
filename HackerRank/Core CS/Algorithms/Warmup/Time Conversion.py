#!/bin/python3

# Get the time string
time = input()
# Split the time into hours, minutes, seconds (with the AM/PM trailing)
h, m, s = time.split (':')

hour = 0

# Check which half of the day it is and compensate
if (time [len(time):len(time) - 3:-1] == "MP"):
    if (int (h) != 12):
        hour += 12
else:
    if (int (h) == 12):
        hour += 12

hour += int (h)

if (hour == 24):
    hour = 0
    
print ("%02d:%02d:%02d" % (hour, int (m), int (s[0:2:1])))
