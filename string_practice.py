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

# strs = ["flowers" , "flow" , "fly", "flight" ]

# first = strs[0]

# for i in range(len(first)):
#             for s in strs[1:]:
#                 if i >= len(s) or first[i] != s[i]:
#                     return first[:i]

#         return first

# 252. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input : s = "egg" , t = "add"

# Output : true

# Explanation :

# The 'e' in string s can be replaced with 'a' of string t.

# The 'g' in string s can be replaced with 'd' of t.

# Hence all characters in s can be replaced to get t.

# Example 2:
# Input : s = "apple" , t = "bbnbm"

# Output : false

# Explanation :

# Strings are matched index by index.

# At index 0, 'a' maps to 'b'.

# At index 1, 'p' also maps to 'b'.

# This is invalid because two different characters (a and p) cannot map to the same character (b) in a one-to-one mapping.

# Therefore, no valid mapping exists and the output is false.
# s = input("Enter a String S = ")
# t = input("Enter a String T = ")

# s_to_t = {}
# t_to_s = {}

# for i in range(len(s)):
    
#     a = s[i]
#     b = t[i]
    
#     if a in s_to_t and s_to_t[a] != b:
#         print("False")
#         break
    
#     if b in t_to_s and t_to_s[b] != a:
#         print("False")
#         break
        
#     s_to_t[a] = b
#     t_to_s[b] = a
    
# print("True")

# 324. Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:
# Input : s = "abcde" , goal = "cdeab"

# Output : true

# Explanation :

# After performing 2 shifts we can achieve the goal string from string s.

# After first shift the string s is => bcdea

# After second shift the string s is => cdeab.

# Example 2:
# Input : s = "abcde" , goal = "adeac"

# Output : false

# Explanation :

# Any number of shift operations cannot convert string s to string goal.

# s = input("enter s = ")
# goal = input("enter goal = ")

# if len(s) != len(goal):
#     print("false")
    
# for i in range(len(s)):
#     if s == goal:
#         print("true")
#         break
#     s = s[1:] + s[0]
    
# print("false")

# return len(s) == len(goal) and goal in (s+s)  #more optimized approach

# s = input("enter s = ")
# t = input("enter t = ")

# if len(s) != len(t):
#     print("false")

    
# for ch in s:
#     if s.count(ch) != t.count(ch):
#         print("false")
    
#     print("true")

# t = sorted(s)
# result = []

# for ch in t:
#     if ch not in result:
#         result.append(ch)

# print(result)


# 79. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input : str = ["flowers" , "flow" , "fly", "flight" ]

# Output : "fl"

# Explanation :

# All strings given in array contains common prefix "fl".

# Example 2:
# Input : str = ["dog" , "cat" , "animal", "monkey" ]

# Output : ""

# Explanation :

# There is no common prefix among the given strings in array.

# str = input('Enter string = ')
# prefix = str[0]

# for s in str[1:]:
#     while not s.startswith(prefix):
#         prefix = prefix[:-1]
        
#     if prefix == "":
#         print("")
        
# print(prefix)
        
