# Q3: A town's current population is 10,000 and it increases by 10% every year.
# Write a program to display the population for the last 10 years.

cur_pop = 10000

for i in range(10, 0, -1):
    print(i, cur_pop)
    cur_pop = cur_pop / 1.1