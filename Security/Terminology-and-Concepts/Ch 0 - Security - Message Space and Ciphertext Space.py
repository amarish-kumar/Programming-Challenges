vals = list (input ())

vals = [int (t) for t in vals]
string = ""

for i in range (0, len (vals), 1):
    vals [i] += 1
    
    if (vals [i] > 9):
        vals [i] = 0
        
    string += str (vals [i])

print (string)
