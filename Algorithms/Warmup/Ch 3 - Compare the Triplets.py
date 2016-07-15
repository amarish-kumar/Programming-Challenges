# Read value triplets and convert to int
inA = [int (val) for val in input ().split (' ')]
inB = [int (val) for val in input ().split (' ')]

# Set up scores
scoreA = 0
scoreB = 0

# Compare each set of two scores to see who won
for i in range (0, 3):
    # If A > B, A won a point
    if inA [i] > inB [i]:
        scoreA += 1
    # If A < B, B won a point
    elif inA [i] < inB [i]:
        scoreB += 1
    # If A == B, nobody wins
    
# Print scores to console
print ("%d %d" % (scoreA, scoreB))
