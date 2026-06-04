# Start.
# Read the number n.
# Set result = 1.
# Repeat for every number from 1 to n:
# Multiply result by the current number.
# Store the answer back in result.
# After the loop ends, result contains the factorial.
# Print result.
# Stop.

number = 5
result = 1
for num in range(1,number +1):
    result = result * num
print(result)
