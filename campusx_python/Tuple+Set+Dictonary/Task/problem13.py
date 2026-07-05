# Q3`: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
# Example 1:
# Input:
# ```bash
# test_list = ["DataScience", 3, "is", 8]
# key_list = ["name", "id"]
# ```
# Output:
# ```bash
# [{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]

test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]

l = []

for i in range(0, len(test_list), 2):
    d = {
        key_list[0]: test_list[i],
        key_list[1]: test_list[i+1]
    }
    l.append(d)

print(l)