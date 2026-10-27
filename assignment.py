n = int(input("Enter a number: "))

# 1
# 1 2
# 1 2 3
# 1 2 3 4


# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end = " ")
#     print()

# or
    
# for i in range(1 , n+1):
#     print(*range(1,i+1))
# A 
# A B 
# A B C 
# A B C D 

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()

# for i in range(1 , n+1):
#     print(*chr(65+i))

# A B C
# A B C
# A B C

# for i in range(n):
#     for j in range(n):
#         print(chr(65 + j), end=" ")
#     print()

#    A
#   BBB
#  CCCCC
# DDDDDDD

# for i in range(n):
#     for s in range(n-1-i):
#         print(" ",end="")
#     for j in range(2*i + 1):
#         print(chr(65+i), end="")
#     print()

# christmas tree
def tree(n):
    for i in range(n):
        for s in range(n-1-i):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()

for i in range(n):
    tree(n)
    
for i in range(1,n+1):
        
        if n % 2 == 0:  
            print(" "*(n//2)+"*"*(n//2),end=" ")
            print()
                 
        else:
            print(" "*(n-2)+"*"*(n//2),end=" ")
            print()

# num = 1
# for i in range(n):
#     for j in range(i+1):
#         print(num, end=" ")
#         num += 1
#     print()



# *       *
#   *   *
#     *
#   *    *
# *        *

# def upper(n):
#     for i in range(n):
#         for s in range(i):
#             print(" ",end="")
        
#         print("*",end="")
        
#         for s in range(2*(n-i-1)-1):
#             print(" ",end="")
        
#         if i != n - 1:
#             print("*",end="")
        
#         print()        
        
# def lower(n):
#     for i in range(n-2,-1,-1):
#         for s in range(i):
#             print(" ",end="")
        
#         print("*",end="")
        
#         for s in range(2*(n-i-1)-1):
#             print(" ",end="")
        
#         if i != n - 1:
#             print("*",end="")
        
#         print() 
        
# upper(n)
# lower(n)

