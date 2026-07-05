# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:

# ['1ac21', '23fg', '456', '098d','1','kls']
# Output:

# ['456', '23fg', '1ac21', '1', 'kls', '098d']

# Problem 7: Sort alphanumeric strings based on product value of numeric characters

# Given list
a = ['1ac21', '23fg', '456', '098d', '1', 'kls']

# Function to calculate product of numeric characters
def product_value(s):
    
    # Start product as 1 (for strings with no numbers)
    product = 1
    
    # Check each character in string
    for i in s:
        
        # If character is a digit, multiply it
        if i.isdigit():
            product = product * int(i)
            
    return product

# Sort list based on product value
result = sorted(a, key=product_value)

# Print final result
print(result)