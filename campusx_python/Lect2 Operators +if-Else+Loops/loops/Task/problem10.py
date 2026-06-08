# Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

for num in range(1000, 3001):
    temp = num
    is_even = True
    
    while temp > 0:
        digit = temp % 10
        if digit % 2 != 0:
            is_even = False
            break
        temp = temp // 10
    
    if is_even:
        print(num, end=" ")