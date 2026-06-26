# ### `Problem 5:` Write a Python function to check whether a number is perfect or not.

# A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

# Example : 

# The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect(s):
    w=0
    d=""
    for i in range(1,s+1):
        if s%i==0:
            w=w+i
    print(w)
    if s==(w/2):
        d="The number is a perfect number"
    else:
        d="The number is not a perfect number"
    return d
    
    

s=int(input("Enter a perfect number:"))
q=perfect(s)
print(q)