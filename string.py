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
s = input("Enter String = ")
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
