input ()

arr = [int (arr_temp) for arr_temp in input().split(' ')]

print (" ".join (str (item) for item in arr[::-1]))
