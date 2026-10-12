
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

# *********
#  *******
#   *****
#    ***
#     *

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(n-i) -1):
        print("*",end="")
    print()