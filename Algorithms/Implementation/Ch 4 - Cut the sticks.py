#!/bin/python3

import sys

def findSmallestStick (array):
    smallest = 1001
    
    for item in array:
        if item < smallest:
            smallest = item
    
    return (smallest)

def cutSticks (array):
    length = len (array)
    cuts = 0
    
    if length == 0:
        return cuts
    
    smallest = findSmallestStick (array)
    newArray = []
    
    for i in range (0, length, 1):
        array[i] -= smallest
        cuts += 1
        
        if array[i] > 0:
            newArray.append (array[i])
    
    print ("%d" % cuts)
    del array
    
    cutSticks (newArray)
    
    return (cuts)
    
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

cutSticks (arr)
