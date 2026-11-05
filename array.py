# Given an array arr of size n, the task is to find the sum of all the elements in the array.

# Example 1:
# Input: n=5, arr = [1,2,3,4,5]

# Output: 15

# Explanation: Sum of all the elements is 1+2+3+4+5 = 15

# Example 2:
# Input: n=6, arr = [1,2,1,1,5,1]

# Output: 11

# Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11

# arr = list(map(int, input("Enter array elements: ").split()))
# n = len(arr)

# def sum(arr, n):
#     total = 0 

#     for i in range(n):
#         total += arr[i]

#     print(total)
# sum(arr, n)

# Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.

# Example 1:
# Input: n = 5, arr = [1,2,3,4,5]

# Output: True

# Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

# Example 2:
# Input: n = 5, arr = [5,4,6,7,8]

# Output: False

# Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False. Here element 5 is not smaller than or equal to its future elements.

# arr = list(map(int, input("Enter array elements: ").split()))
# n = len(arr)
# for i in range(n-1):
#     if arr[i] > arr[i+1]:
#         print("False")
#         break
#     else:
#         print("True")

# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

# Example 1:
# Input: n=5, arr = [1,2,3,4,5]

# Output: [5,4,3,2,1]

# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

# Example 2:
# Input: n=6, arr = [1,2,1,1,5,1]

# Output: [1,5,1,1,2,1]

# Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].
# for i in range(1):
#  print(arr[::-1])


# 838. Linear Search
# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

# Example 1:
# Input: nums = [2, 3, 4, 5, 3], target = 3

# Output: 1

# Explanation:

# The first occurence of 3 in nums is at index 1

# Example 2:
# Input: nums = [2, -4, 4, 0, 10], target = 6

# Output: -1

# Explanation:

# The value 6 does not occur in the array, hence output is -1

# nums = list(map(int, input("Enter array elements: ").split()))
# n = len(nums)
# target = int(input("enter target = "))
# for i in range(n):
#     if nums[i] == target:
#         print(i)
#         break
# print("-1")

# Majority Element
# A = list(map(int, input("Enter array elements: ").split()))
# n = len(A)
# count = 0

# for i in range(n):
#     for j in range(n):
#         if A[i] == A[j]:
#             count += 1
#     if count > n//2:
#         print(A[i])
#         break
#     else:
#         print("-1")

# 832. Left Rotate Array by One

# Given an integer array nums, rotate the array to the left by one.

# Note: There is no need to return anything, just modify the given array.

# Example 1:
# Input: nums = [1, 2, 3, 4, 5]

# Output: [2, 3, 4, 5, 1]

# Explanation:

# Initially, nums = [1, 2, 3, 4, 5]

# Rotating once to left -> nums = [2, 3, 4, 5, 1]

# Example 2:
# Input: nums = [-1, 0, 3, 6]

# Output: [0, 3, 6, -1]

# Explanation:

# Initially, nums = [-1, 0, 3, 6]

# Rotating once to left -> nums = [0, 3, 6, -1]

nums = list(map(int, input("Enter array elements: ").split()))

n = len(nums)

temp = nums[0]

for i in range(n-1):
    nums[i] = nums[i+1]
nums[n-1] = temp
print(nums)