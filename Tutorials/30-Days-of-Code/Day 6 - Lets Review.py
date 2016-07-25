t = int (input ())

for t in range (0, t, 1):
    word = input ()
    
    evens = ""
    odds = ""
    
    for i in range (0, len (word), 1):
        if (i % 2 == 0):
            evens += word[i]
        else:
            odds += word[i]
    
    print ("%s %s" % (evens, odds))
