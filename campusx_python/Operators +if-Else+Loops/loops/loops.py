# In Python, there are two types of loops:
# 1. While Loop
# 2. For Loop

# ==========================
# While Loop with Else
# ==========================

# The else block executes when the while loop condition becomes False
# and the loop finishes normally (without a break statement).

x = 1

while x < 3:
    print(x)
    x += 1
else:
    print("limit crossed")