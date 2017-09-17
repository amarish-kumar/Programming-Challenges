string = list (input ())

index, char = input ().split (' ')
index = int (index)

string [index] = char

print ("".join (string))