
# 932. Sum of First N Numbers
# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

# Example 1:
# Input : N = 4

# Output : 10

# Explanation : first four natural numbers are 1, 2, 3, 4.

# Sum is 1 + 2 + 3 + 4 => 10.

# Example 2:
# Input : N = 2

# Output : 3

# Explanation : first two natural numbers are 1, 2.

# Sum is 1 + 2 => 3.
# n = int(input("enter N = "))
# def sum(N):
#     if  N == 0:
#         return 0
    
#     Sum = N + sum(N-1)
#     return Sum
   
    
# print(sum(N))

# 921. Factorial of a Given Number
# Given an integer n, return the factorial of n.

# Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n (use 64-bits to return answer).

# Example 1:
# Input : n = 3

# Output : 6

# Explanation : Factorial = 1 * 2 * 3 => 6

# Example 2:
# Input : n = 5

# Output : 120

# Explanation : Factorial = 1 * 2 * 3 * 4 * 5 => 120

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         res = n*factorial(n-1)
#     return res

# print(factorial(n))
       
# nums = [1,2,3,4,5]

# def sum(nums):
#     res = 0
#     for i in range(len(nums)):
#         res = res + nums[i]

#     return res
# print(sum(nums))

# s = ["h", "e", "l", "l", "o"]
# s.reverse()
# print(s)

s = "hah"

# class Solution:
#     def palindromeCheck(s):

#         if len(s) <= 1:
#             return True

#         if s[0] != s[-1]:
#             return False

        
#     print(palindromeCheck(s))

# num = int(input("Enter a num: "))
# def check(i):
#     if i == num:
#         print("True")
    
#     if num % i == 0:
#         print("False")
    
#     return check(i+1)

# if num <= 1:
#     print("False")
    
