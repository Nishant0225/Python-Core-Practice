# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.

# Input:
# hel123O4every093

# Output:
# Sum: 22
# Avg: 2.75

# Take string input from the user
str1 = input("Enter any string: ")
sum=0
count=0
n="0123456789"
for i in str1:
    if i in n:
        sum=sum+int(i)
        count+=1
print("sum:",sum,"avg=",sum/count)
    