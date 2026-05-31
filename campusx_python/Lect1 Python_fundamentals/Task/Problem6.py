# Q6: Write a program to determine the number of dogs and chickens based on the total number of heads and legs provided by the user.
# Example: Input -> heads = 4, legs = 12 | Output -> dogs = 2, chickens = 2

heads=int(input("Enter number of Heads:"))
legs=int(input("Enter number of Legs:"))
 
dogs = (legs - 2 * heads) // 2
chickens = heads - dogs

print("Dogs:", dogs)
print("Chickens:", chickens)