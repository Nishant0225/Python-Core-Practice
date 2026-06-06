# Problem 5: Display Fibonacci Series up to n terms

# Take the number of terms from the user
num = int(input("Enter nth term: "))

# First two terms of the Fibonacci series
a = 0
b = 1

# Print the first two terms
print(0, end=" ")
print(1, end=" ")

# Generate the remaining terms
for i in range(1, num - 1):

    # Next term is the sum of the previous two terms
    k = a + b

    # Print the next term
    print(k, end=" ")

    # Update the values for the next iteration
    a = b
    b = k