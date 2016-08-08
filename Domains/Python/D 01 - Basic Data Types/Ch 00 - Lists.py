n = int (input ())

l = list ()

for i in range (n):
    s = input ().strip ().split (' ')
    
    if (s[0] == "insert"):
        eval ("l.{0} ({1}, {2})".format (*s))
    elif (s[0] == "print"):
        print (l)
    else:
        eval ("l.{0} ({1})".format (*s + ['']))