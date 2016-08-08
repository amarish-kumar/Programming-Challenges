n = int (input ())

scoreBook = dict ()

for i in range (0, n, 1):
    name, s1, s2, s3 = input ().split (' ')
    s1, s2, s3 = [float (s1), float (s2), float (s3)]
    
    scoreBook [name] = (s1 + s2 + s3) / 3
    
selectedName = input ()

print ("%0.2f" % scoreBook[selectedName])