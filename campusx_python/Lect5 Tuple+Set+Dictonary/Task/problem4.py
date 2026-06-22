#  Count no of tuples, list and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

# Output:

# List-2
# Set-2
# Tuples-1


a = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
listt,sett,tupless,other=0,0,0,0
print(type(a))
for i in a:
    if type(i)==list:
        listt+=1
    elif type(i)==tuple:
        tupless+=1
    elif type(i)==set:
        sett+=1
    else:
        other+=1
print("number of list=",listt)
print("number of sets=",sett)
print("number of tuple=",tupless)
print("number of other elements=",other)
        