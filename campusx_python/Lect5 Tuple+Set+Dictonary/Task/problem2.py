# Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
# For eg.

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)

# Original tuple
t = (1, 5, 7, 8, 10)

# List to store the result
result = []

for i in range(len(t)):

    # First element
    if i == 0:
        result.append(t[i] * t[i + 1])

    # Last element
    elif i == len(t) - 1:
        result.append(t[i] * t[i - 1])

    # Middle elements
    else:
        result.append((t[i] * t[i - 1]) + (t[i] * t[i + 1]))

# Convert list into tuple
result = tuple(result)

print(result)