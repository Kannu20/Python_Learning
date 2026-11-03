
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

# from pyparsing import nums


# s = "hah"

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
    

# 821. Reverse an array 2
# Given an array nums of n integers, return reverse of the array.

# Example 1:
# Input : nums = [1, 2, 3, 4, 5]

# Output : [5, 4, 3, 2, 1]

# Example 2:
# Input : nums = [1, 3, 3, 3, 5]

# Output : [5, 3, 3, 3, 1]




# nums = [1, 2, 3, 4, 5]

# nums = [1, 3, 3, 3, 5]
# print(nums[::-1])

# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

# Example 1:
# Input : nums = [1, 2, 3, 4, 5]

# Output : true

# Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

# Example 2:
# Input : nums = [1, 2, 1, 4, 5]

# Output : false

# Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

# num = list(map(int, input("Enter the elements of the array separated by space: ").split()))
# def check(i):
    
#     if i == len(num)-1:
#         return True

#     if num[i] > num[i+1]:
#         return False
    
#     return check(i+1)

# print(check(0))

# 965. Sum of Digits in a Given Number
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input : num = 529

# Output : 7

# Explanation : In first iteration the digits sum will be = 5 + 2 + 9 => 16

# In second iteration the digits sum will be 1 + 6 => 7.

# Now single digit is remaining , so we return it.

# Example 2:
# Input : num = 101

# Output : 2

# Explanation : In first iteration the digits sum will be = 1 + 0 + 1 => 2

# Now single digit is remaining , so we return it.
# num = int(input("Enter a num: "))
# def sumOfDigits(num):
#     if num < 10:
#         return num
#     else:
#         return sumOfDigits(sum(int(digit) for digit in str(num)))
    
# print(sumOfDigits(num))


from pyparsing import nums


num = [3,2,5,1,6,7,8,9,12]

# def sum(num):
#     if len(num) == 0:
#         return 0
    
#     return num[0] + sum(num[1:])

# print(sum(num))

# Linear Search using recursion
# target = int(input("Enter the target: "))

# def linearSearch(num, target, index):
    
#     # Base Case
#     if index == len(num):
#         return -1
    
#     if num[index] == target:
#         return index
    
#     return linearSearch(num, target, index + 1)

# print(linearSearch(num, target, 0))

 
# Binary Search using recursion
# key = int(input("Enter the key: "))
# def binarySearch(num, start, end, key):
    
#     if start > end:
#         return False
    
#     mid = start + (end - start) // 2
    
#     if num[mid] == key:
#         return mid
    
#     if num[mid] < key:
#         return binarySearch(num, mid + 1, end, key)
    
#     else:
#         return binarySearch(num, start, mid - 1, key)
    
# print(binarySearch(num, 0,len(num)-1,key))
# nums= [1,2,3,5,4,3]
# target = 3
# def binary(nums, start, end, target):
#     if start > end:
#         return min(nums)

#     mid = start + (end - start) // 2

#     if nums[mid] == target:
#         return mid

#     if nums[mid] < target:
#         return binary(nums, mid + 1, end, target)

#     if nums[mid] > target:
#         return binary(nums, start, mid - 1, target)
            
# print(binary(nums, 0, len(nums) - 1, target))


# 729. Lower Bound
# Given a sorted array of nums and an integer x, write a program to find the lower bound of x.

# The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# If no such index is found, return the size of the array.

# Example 1:
# Input : nums= [1,2,2,3], x = 2

# Output:1

# Explanation:

# Index 1 is the smallest index such that arr[1] >= x.

# Example 2:
# Input : nums= [3,5,8,15,19], x = 9

# Output: 3

# Explanation:

# Index 3 is the smallest index such that arr[3] >= x.
# nums= [1, 2, 2, 2, 3]
# x = 2
# def binary(nums, start, end, x):
    
#     if start > end:
#         return start
    
#     mid = start + (end - start) // 2


#     if nums[mid] < x:
#         return binary(nums, mid + 1, end, x)
    
#     else:
#         return binary(nums, start, mid - 1, x)

# print(binary(nums, 0, len(nums) - 1, x))

# 750. Upper Bound
# Given a sorted array of nums and an integer x, write a program to find the upper bound of x.

# The upper bound of x is defined as the smallest index i such that nums[i] > x.

# If no such index is found, return the size of the array.

# Example 1:
# Input : n= 4, nums = [1,2,2,3], x = 2

# Output:3

# Explanation:

# Index 3 is the smallest index such that arr[3] > x.

# Example 2:
# Input : n = 5, nums = [3,5,8,15,19], x = 9

# Output: 3

# Explanation:

# Index 3 is the smallest index such that arr[3] > x.
nums = [1,2,2,3]
x = 2
def binary(nums, start, end, x):
        if start > end:
            return start

        mid = start + (end - start) // 2

        if nums[mid] <= x:
            return binary(nums, mid + 1, end, x)

        else:
            return binary(nums, start, mid - 1, x)
print(binary(nums, 0, len(nums)-1,x))