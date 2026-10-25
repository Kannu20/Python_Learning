n = int(input("Enter a number: "))

# 1
# 1 2
# 1 2 3
# 1 2 3 4


# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end = " ")
#     print()
    
# A 
# A B 
# A B C 
# A B C D 

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()

# A B C
# A B C
# A B C

# for i in range(n):
#     for j in range(n):
#         print(chr(65 + j), end=" ")
#     print()


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


def upper():
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for s in range(2*(n-i-1)):
            print(" ", end="")
        for j in range(i+1):
             print("*",end="")
        print()
        
def lower():
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end="")
        for s in range(2*(i+1)):
            print(" ",end="")
        for j in range(n-i-1):
            print("*",end="")
        print()
    
upper()
lower()