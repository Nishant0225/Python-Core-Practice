# Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

# For eg.

# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

d = {}

# Group values having the same first element
for i in test_list:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])

result = []

# Convert dictionary back to tuples
for key in d:
    result.append((key, *d[key]))

print(result)