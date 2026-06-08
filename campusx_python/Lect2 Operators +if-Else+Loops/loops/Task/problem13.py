# Problem 13:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

r=int(input("Enter range"))
for i in range(1,r):
    temp=0
    sq=0
    temp=i
    while temp!=0:
        digit=temp%10
        sq=sq+(digit*digit*digit)
        temp=temp//10
    if sq==i:
        print(i)
    
        