# login program 

email=input("Enter email: ")
password=input("Enter password: ")

# if email== "tanvi@gmail.com" and password== "1234":
#     print("Login successful")
# else:
#     print("Login failed")

if email== "tanvi@gmail.com" and password== "1234":
    print("Login successful")
elif email== "tanvi@gmail.com" and password != "1234":
    print("Incorrect Password")
    password=input("Enter password again: ")
    if password== "1234":
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Login failed")
    
    
#find min of 3 no
aa=int(input("1st"))
bb=int(input("2nd"))
cc=int(input("3rd"))

if aa>bb and aa>cc:
    print('a is greatest')
elif bb>cc:
    print('b is greatest')
else:
    print('c is greatest')
    