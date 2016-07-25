def product (arr):
    total = 1
    
    for item in arr:
        total *= item
        
    return (total)
    
# Get the number of test cases
t = int (input ())

# Go through each test case
for i in range (0, t, 1):
    # Get the values n (length of sequence), k (length of product)
    n, k = input ().split (' ')
    n, k = [int (n), int (k)]
    # Get the sequence
    num = list (input ())
    num = [int (temp) for temp in num]
      
    biggest = 0 # The largest product
    current = 0 # The current product
        
    # Move through the sequence in blocks of k
    for j in range (0, n - k + 1, 1):
        # Take the product of the k block
        current += product (num [j:j + k:1])
        
        # Check if it is the new largest
        if (current > biggest):
            biggest = current
            
        current = 0
        
    print ("%d" % biggest)
    
   
