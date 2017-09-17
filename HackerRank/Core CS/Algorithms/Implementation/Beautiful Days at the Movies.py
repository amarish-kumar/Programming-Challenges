# Python 3.5

i, j, k = list (map (int, input ().split (' ')))

total_days = 0

for index in range (i, j + 1, 1):
    i_reversed = int ("".join (list (reversed (list (str (index))))))

    if (abs (index - i_reversed) % k == 0):
        total_days += 1

print (total_days)
