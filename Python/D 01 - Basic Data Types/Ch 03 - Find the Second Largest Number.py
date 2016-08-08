# Get worthless length value
input ()
# Save array of num as set to remove duplicates, then turn into list
arr = list ({int (temp) for temp in input ().split (' ')})

# Remove max value from list
arr.remove (max (arr))

# Print second biggest value
print (max (arr))