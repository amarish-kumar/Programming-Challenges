# The sum of squares is the sum of each value <= n squared, and summed
def sumSquares (n):
    sum = 0
    
    for i in range (1, n + 1, 1):
        sum += i * i
        
    return (sum)

# The square of the sums is the sum of each value <= n, squared
def squareSum (n):
    sum = 0
    
    for i in range (1, n + 1, 1):
        sum += i

    return (sum * sum) 

# Sum square difference is the square of the sum minus the sum of squares
def sumSquareDiff (n):
    return (squareSum (n) - sumSquares (n))

# Get the number of test cases
t = int (input ())

# Go through each test case
for i in range (0, t, 1):
    # Get the value to be counted towards
    n = int (input ())
    
    # Print the sum square difference
    print ("%d" % sumSquareDiff (n))
