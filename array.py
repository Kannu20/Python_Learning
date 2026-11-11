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
# Brute Force Approach it will give TLE for large input
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

# Optimal Approach By Using Boyer-Moore Voting Algorithm

# What is this algorithm?
# The Boyer-Moore Voting Algorithm is an efficient algorithm used to find the majority element in an array. A majority element is defined as an element that appears more than n/2 times in the array, where n is the size of the array.

# candidate = None
# count = 0

# for num in A:
    
#     if count == 0:
#         candidate= num
    
#     if num == candidate:
#         count += 1
#     else:
#         count -= 1
    
# print(candidate)

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

# nums = list(map(int, input("Enter array elements: ").split()))

# n = len(nums)

# temp = nums[0]

# for i in range(n-1):
#     nums[i] = nums[i+1]
# nums[n-1] = temp
# print(nums)  


# 248. Move Zeros to End

# Companies
# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.

# This must be done in place, without making a copy of the array.

# Example 1:
# Input: nums = [0, 1, 4, 0, 5, 2]

# Output: [1, 4, 5, 2, 0, 0]

# Explanation:

# Both the zeroes are moved to the end and the order of the other elements stay the same

# Example 2:
# Input: nums = [0, 0, 0, 1, 3, -2]

# Output: [1, 3, -2, 0, 0, 0]

# Explanation:

# All 3 zeroes are moved to the end and the order of the other elements stay the same
# nums = [0,0, 0, 1, 3, -2]
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == 0:
#             nums[i], nums[j] = nums[j], nums[i]
            
# print(nums)

# 196. Remove duplicates from sorted array
# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once.

# Return the number of unique elements in the array.

# If the number of unique elements be k, then,

# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.
# The driver code will assess correctness by printing and checking only the first k elements of the modified array.
# An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.

# Example 1:
# Input: nums = [0, 0, 3, 3, 5, 6]

# Output: 4

# Explanation:

# Resulting array = [0, 3, 5, 6, _, _]

# There are 4 distinct elements in nums and the elements marked as _ can have any value.

# Example 2:
# Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]

# Output: 4

# Explanation:

# Resulting array = [-2, 2, 4, 5, _, _, _, _]

# There are 4 distinct elements in nums and the elements marked as _ can have any value.

# nums = list(map(int, input("Enter array = ").split()))
# i = 0

# for j in range(1, len(nums)):
#     if nums[i] != nums[j]:
#         i += 1
#         nums[i] = nums[j]
    
# print(nums[:i+1])

# 116. Find missing number
# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

# Example 1:
# Input: nums = [0, 2, 3, 1, 4]

# Output: 5

# Explanation:

# nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

# Example 2:
# Input: nums = [0, 1, 2, 4, 5, 6]

# Output: 3

# Explanation:

# nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]


# nums = [0, 1, 2, 4, 5, 6]
# n = len(nums)

# expected_sum = n * (n + 1) // 2 # this formula calculates the sum of the first n natural numbers
# actual_sum = sum(nums)
# missing_number = expected_sum - actual_sum
# print(missing_number)

# 713. Union of two sorted arrays
# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.

# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

# Example 1:
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

# Output: [1, 2, 3, 4, 5, 7]

# Explanation:

# The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

# Example 2:
# Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

# Output: [1, 3, 4, 5, 6, 7, 8, 9]

# Explanation:

# The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2


# nums1 = [3, 4, 6, 7, 9, 9]
# nums2 = [1, 5, 7, 8, 8]


# a = set(nums1)
# b = set(nums2)

# c = a | b
# print(sorted(c))

# 706. Intersection of two sorted arrays
# Given two sorted arrays, nums1 and nums2, return an array containing the intersection of these two arrays. Each element in the result must appear as many times as it appears in both arrays; that is, if an element appears x times in nums1 and y times in nums2, it should appear min(x, y) times in the result.

# The intersection of two arrays is an array where all values are present in both arrays. Since both input arrays are sorted, the resulting intersection array should also be in sorted order.

# Example 1:
# Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]

# Output: [1, 2]

# Explanation:

# The elements 1, 2 are the only elements present in both nums1 and nums2

# Example 2:
# Input: nums1 = [1, 2, 2, 3, 3, 3], nums2 = [2, 3, 3, 4, 5, 7]

# Output: [2, 3, 3]

# Explanation:

# The element 2 appears in both arrays only one time.

# The element 3 appears in both arrays two times so we add element 3 equal to its number of occurrences.
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 7,]
# i = 0
# j = 0
# result = []

# while i < len(nums1) or j < len(nums2):
#     if nums1[i] < nums2[j]:
#         result.append(nums1[i])
#         result.append(nums2[j])
#         i += 1
#         j += 1
        
#     elif nums1[i] > nums2[j]:
#         result.append(nums1[i])
#         result.append(nums2[j])
#         i += 1
#         j += 1
        
#     else:
#         result.append(nums1[i])
#         i += 1
#         j += 1
        
# print(result)
    
# 706. Intersection of two sorted arrays
# Given two sorted arrays, nums1 and nums2, return an array containing the intersection of these two arrays. Each element in the result must appear as many times as it appears in both arrays; that is, if an element appears x times in nums1 and y times in nums2, it should appear min(x, y) times in the result.

# The intersection of two arrays is an array where all values are present in both arrays. Since both input arrays are sorted, the resulting intersection array should also be in sorted order.

# Example 1:
# Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]

# Output: [1, 2]

# Explanation:

# The elements 1, 2 are the only elements present in both nums1 and nums2

# Example 2:
# Input: nums1 = [1, 2, 2, 3, 3, 3], nums2 = [2, 3, 3, 4, 5, 7]

# Output: [2, 3, 3]

# Explanation:

# The element 2 appears in both arrays only one time.

# The element 3 appears in both arrays two times so we add element 3 equal to its number of occurrences.

# i = 0
# j = 0
# result = []

# while i < len(nums1) and j < len(nums2):
#     if nums1[i] < nums2[j]:
#         i += 1
#     elif nums1[i] > nums2[j]:
#         j += 1
    
#     else:
#         result.append(nums1[i])
#         i += 1
#         j += 1
        
# print(result)

# 512. Leaders in an Array
# Given an integer array nums, return a list of all the leaders in the array.

# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

# Example 1:
# Input: nums = [1, 2, 5, 3, 1, 2]

# Output: [5, 3, 2]

# Explanation:

# 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

# Example 2:
# Input: nums = [-3, 4, 5, 1, -4, -5]

# Output: [5, 1, -4, -5]

# Explanation:

# -5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]

# nums = [-3, 4, 5, 1, -4, -5]
# result = []

# max = nums[-1]
# result.append(max)

# for i in range(len(nums)-2, -1, -1):
    
#     if nums[i] > max:
#         result.append(nums[i])
#         max = nums[i]
        
# print(result[::-1])

# 375. Rearrange array elements by sign
# Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Example 1:
# Input : nums = [2, 4, 5, -1, -3, -4]

# Output : [2, -1, 4, -3, 5, -4]

# Explanation:

# The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

# nums = [2, 4, 5, -1, -3, -4]
# n = len(nums)
# result = [0] * n
# pos = 0
# neg = 1

# for num in nums:
    
#     if num > 0:
#         result[pos] = num
#         pos += 2
        
#     else:
#         result[neg] = num
#         neg += 2
        
# print(result)


# 107. Print the matrix in spiral manner
# Given an M * N matrix, print the elements in a clockwise spiral manner.

# Return an array with the elements in the order of their appearance when printed in a spiral manner.

# Example 1:
# Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Explanation:

# The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

# Example 2:
# Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

# Output: [1, 2, 3, 4, 8, 7, 6, 5]

# Explanation:

# The elements in the spiral order are 1, 2, 3, 4 -> 8, 7, 6, 5

# matrix = [[1],[2],[4],[3],[5]]
# result = []
# top = 0
# bottom = len(matrix) - 1

# right = len(matrix[0]) - 1
# left = 0
# while top <= bottom and left <= right:
#     for i in range(left, right + 1):
#         result.append(matrix[top][i])
#     top += 1

#     for i in range(top , bottom + 1):
#         result.append(matrix[i][right])
        
#     right -= 1

#     if top <= bottom:
#         for i in range(right, left - 1, -1):
#             result.append(matrix[bottom][i])
            
#         bottom -= 1

#     if left <= right:
#         for i in range(bottom, top-1, -1):
#             result.append(matrix[i][left])

#         left += 1

# print(result)

# 161. Pascal's Triangle I
# Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.

# In Pascal's triangle:

# The first row contains a single element 1.
# Each row has one more element than the previous row.
# Every row starts and ends with 1.
# For all interior elements (i.e., not at the ends), the value at position (r, c) is computed as the sum of the two elements directly above it from the previous row:

# Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
# where indexing is 1-based
# Example 1:
# Input: r = 4, c = 2

# Output: 3

# Explanation:

# The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# ....

# Thus, value at row 4 and column 2 = 3

# Example 2:
# Input: r = 5, c = 3

# Output: 6

# Explanation:

# The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# 1 4 6 4 1

# ....

# Thus, value at row 5 and column 3 = 6
# r = 4
# c = 2
# prev = [1]

# for i in range(1, r):
#     curr = [1]

#     for j in range(1, i):
#         curr.append(prev[j-1] + prev[j])

#     curr.append(1)
#     prev = curr

# print(prev[c-1])

# 378. Pascal's Triangle II
# Given an integer r, return all the values in the rth row (1-indexed) in Pascal's Triangle in correct order.

# In Pascal's triangle:

# The first row has one element with a value of 1.
# Each row has one more element in it than its previous row.
# The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.
# Example 1:
# Input: r = 4

# Output: [1, 3, 3, 1]

# Explanation:

# The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# ....

# Thus the 4th row is [1, 3, 3, 1]

# Example 2:
# Input: r = 5

# Output: [1, 4, 6, 4, 1]

# Explanation:

# The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# 1 4 6 4 1

# ....

# Thus the 5th row is [1, 4, 6, 4, 1]
# r = 4
# prev = [1]

# for i in range(1, r):
#     curr = [1]
    
#     for j in range(1, i):
#         curr.append(prev[j-1] + prev[j])
        
#     curr.append(1)
#     prev = curr
# print(prev)

# 945. Pascal's Triangle III
# Given an integer n, return the first n (1-Indexed) rows of Pascal's triangle.

# In Pascal's triangle:

# The first row has one element with a value of 1.
# Each row has one more element in it than its previous row.
# The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.
# Example 1:
# Input: n = 4

# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

# Explanation: The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# 1st Row has its value set to 1.

# All other cells take their value as the sum of the values directly above them

# Example 2:
# Input: n = 5

# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Explanation: The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# 1 4 6 4 1

# 1st Row has its value set to 1.

# All other cells take their value as the sum of the values directly above them

n = 5
prev = [1]
ans = []
for i in range(1,n+1):
    curr = [1]
    
    for j in range(1,i):
        curr.append(prev[j-1] + prev[j])
        
    curr.append(1)
    ans.append(prev)
    prev = curr
print(ans)