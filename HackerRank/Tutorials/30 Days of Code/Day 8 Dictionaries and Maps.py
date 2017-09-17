n = int (input ())

phoneBook = dict ()

for i in range (0, n, 1):
    name, num = input ().split (' ')
    
    phoneBook[name] = num
    
for i in range (0, n, 1):
    name = input ()
    
    if (name in phoneBook):
        print ("%s=%s" % (name, phoneBook[name]))
    else:
        print ("Not found")
