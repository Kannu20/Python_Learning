
# Q1 
# *****

# *****

# *****

# *****

# *****

# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# Q2
# *

# **

# ***

# ****

# *****

# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")     
#     print()

# Q3

# 1

# 12

# 123

# 1234

# 12345

# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()

# Q4
# 1

# 22

# 333

# 4444

# 55555

# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()

# Q5
# *****

# ****

# ***

# **

# *

# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n-i):
#         print("*", end='')
#     print()
        
      
# Q6

# 12345

# 1234

# 123

# 12

# 1  
# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end="")
#     print()
    
# Q7

#     *
#    ***
#   *****
#  *******
# *********

# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()

# Q8
# *********
#  *******
#   *****
#    ***
#     *

n = int(input('Enter a number: '))

# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*(n-i) -1):
#         print("*",end="")
#     print()

# Q9
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# def upper():
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for k in range(2*i+1):
#             print("*",end="")
#         print()

# def lower():
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for k in range(2*(n-i) -1):
#             print("*",end="")
#         print()
        
# upper()
# lower()

# Q10
# *
# **
# ***
# ****
# ***
# **
# *

# def upper():
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
#         print()
# def lower():
#     for i in range(n):
#         for j in range(n-i-1):
#             print("*",end="")
#         print()
        
# upper()
# lower()

# Q11
# 1 

# 0 1 

# 1 0 1 

# 0 1 0 1 

# 1 0 1 0 1

# for i in range(n):
#     for j in range(i+1):
#         if (i+j)%2 == 0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

def right():
    for i in range(n):
        # left pattern
        for j in range(i+1):
            print(j+1,end="")
        # Space
        for k in range(2*(n-i-1)):
            print(" ",end="")
        # right pattern
        for j in range(1+i,0,-1):
            print(j,end="")
        print()
right()