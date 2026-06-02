# Convert a string to title case without using the title() function
# Example:
# Input  : "hello how are you"
# Output : "Hello How Are You"

a=input("Enter a string")
l=[]
for i in a.split():
    l.append(i[0].upper()+i[1::].lower())
    
print(" ".join(l))
    
    
        