t1, t2, n = input ().strip ().split (' ')
t1, t2, n = [int(t1),int(t2),int(n)]

for i in range (0, n - 2, 1):
    
    t3 = t1 + (t2 * t2)
    
    t1 = t2
    t2 = t3
    
print ("%d" % t3)
