#  Add Space between Potential Words.
# Example:

# Input:

# ['campusxIs', 'bestFor', 'dataScientist']
# Output:

# ['campusx Is', 'best For', 'data Scientist']

# Add space between potential words (CamelCase splitting)

# Given list
a = ['campusxIs', 'bestFor', 'dataScientist']

# Empty list to store final results
b = []

# Loop through each word in the list
for i in a:
    
    # Temporary string for building each word
    s = ""
    
    # Traverse each character
    for j in i:
        
        # If uppercase letter found, add space before it
        if 'A' <= j <= 'Z':
            s = s + " "
        
        # Add character to result string
        s = s + j
    
    # Add processed string to result list
    b.append(s)

# Print final result
print(b)
        
    
        