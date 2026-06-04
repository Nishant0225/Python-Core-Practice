# Problem 6: Find the factorial of a given number.

# Write a program that uses a loop to find the factorial of a given number.

# The factorial (symbol: !) of a number is the product of all
# positive integers from that number down to 1.

# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120 n=n

# Input:
# 5

# Output:
# 120 

a=int(input("Enter number for finding factorial:"))
temp=1
for i in range(1,a+1):
    temp=temp*i
    
print(temp)
    
    
    