# # # Problem 2:
# # # Print the following star pattern:
# # #
# # # *
# # # * *
# # # * * *
# # # * * * *
# # # * * * * *
# # # * * * *
# # # * * *
# # # * *
# # # *
# # #
# # # First print stars in increasing order from 1 to 5,
# # # then print stars in decreasing order from 4 to 1.

# # a=int(input('Enter Rows'))
# # b="*"
# # for i in range(1,a+1,1):
# #     for j in range(1,i+1,1):
# #         print(b,end="")
# #     print()
# # for k in range(a-1,1,-1):
# #     for j in range(k,1,-1):
# #         print(b,end="")
# #     print()
# # Problem 2: Print the following pattern.

# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# # * * * * 
# # * * * 
# # * * 
# # *


# num=int(input("Enter no of rows: " ))



# for i in range(1,(num//2+1)+1):
#     for j in range(1,i+1):
#         print("* ",end='')
#     print()

# for k in range(num//2,0,-1):
#     for l in range(k,0,-1):
#         print("* ",end='')
#     # print(