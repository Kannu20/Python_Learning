
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

# Q12

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

# def right():
#     for i in range(n):
#         # left pattern
#         for j in range(i+1):
#             print(j+1,end="")
#         # Space
#         for k in range(2*(n-i-1)):
#             print(" ",end="")
#         # right pattern
#         for j in range(1+i,0,-1):
#             print(j,end="")
#         print()
# right()

# 1 

# 2 3 

# 4 5 6 

# 7 8 9 10 

# 11 12 13 14 15

# num = 1
# for i in range(n):
#     for j in range(i+1):
#         print(num,end=" ")
#         num += 1
#     print()

# Q14
# A 
# A B 
# A B C 
# A B C D 
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()



# if n < 49:
#     print("Enter value greater than 48 to find ASCII")
# else:
#     for i in range(48, n + 1):
#         print(chr(i))

# Q16

# A 
# B B 
# C C C 
# D D D D 

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print()

#    A
#   ABA
#  ABCBA
# ABCDCBA

# for i in range(n):
#     for s in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(65+j),end="")
#     for j in range(i-1,-1,-1):
#         print(chr(65+j),end="")
#     print()

# E 

# D E 

# C D E 

# B C D E 

# A B C D E

# for i in range(n):
#     for j in range(i,-1,-1):
#         print(chr(65+n-1-j),end="")
#     print()

# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********
# def upper():
#     for i in range(n):
#         for j in range(n-i):
#             print("*",end="")
#         for s in range(2*i):
#             print(" ",end="")
#         for j in range(n-i):
#             print("*",end="")
#         print()
        
# def lower():
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
#         for s in range(2*(n-i-1)):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*",end="")
#         print()
        
# upper()
# lower()

def upper():
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for s in range(2*(n-i-1)):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
def lower():
    for i in range(n):
        for j in range(n-1-i):
            print("*",end="")
        for s in range(2*(i+1)):
            print(" ",end="")
        for j in range(n-1-i):
            print("*",end="")
        print()
        
        
upper()
lower()