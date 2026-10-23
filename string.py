# Given a string, the task is to reverse it. The string is represented by an array of characters s.

# Perform the reversal in place with O(1) extra memory.

# Note: no need to return anything, modify the given list.

# Example 1:
# Input : s = ["h", "e" ,"l" ,"l" ,"o"]

# Output : ["o", "l", "l", "e", "h"]

# Explanation :

# The given string is s = "hello" and after reversing it becomes s = "olleh".

# Example 2:
# Input : s = ["b", "y" ,"e" ]

# Output : ["e", "y", "b"]

# Explanation :

# The given string is s = "bye" and after reversing it becomes s = "eyb".
# s = input("Enter String = ")
# for i in range(1):
#     print(s[::-1])


# 895. Palindrome Check
# You are given a string s. Return true if the string is palindrome, otherwise false.

# A string is called palindrome if it reads the same forward and backward.

# Example 1:
# Input : s = "hannah"

# Output : true

# Explanation :

# The given string when read backward is -> "hannah", which is same as when read forward.

# Hence answer is true.

# Example 2:
# Input : s = "aabbaaa"

# Output : false

# Explanation :

# The given string when read backward is -> "aaabbaa", which is not same as when read forward.

# Hence answer is false.

# if s[::] == s[::-1]:
#     print("True")
# else:
#     print("False")

# 341. Largest Odd Number in a String
# Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.

# The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)

# Example 1:
# Input : s = "5347"

# Output : "5347"

# Explanation :

# The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.

# So the largest among all the possible odd numbers for given string is 5347.

# Example 2:
# Input : s = "0214638"

# Output : "21463"

# Explanation :

# The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.

# We cannot include 021463 as the number contains leading zero.

# So largest odd number in given string is 21463.

# s = input("String = ")
# for i in range(len(s)-1,-1,-1):
#     if int(s[i]) % 2 != 0:
#         print(s[:i+1].strip("0"))
#         break
# print("")