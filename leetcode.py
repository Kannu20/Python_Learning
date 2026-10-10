

# s = "IV"

# s1 = range(len(s))

# print(list(s1))


# A = {1, 2, 3}
# B = {4, 5, 6}

# print(A.isdisjoint(B))

# l = {1,2,10,9,6,4}
# print(len(l))

# ROMAN TO INTEGER

# s = input("Enter String: ")

# values = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

# result = 0

# for i in range(len(s)):
#     if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
#         result = result - values[s[i]]
#     else:
#         result += values[s[i]]
    
# print(result)

# 58. Length of Last Word
# s = input("Enter a string: ")

# s = s.strip()
# count = 0

# for i in range(len(s) - 1, -1, -1):
#     if s[i] == " ":
#         break
#     count += 1

# print(count)

# 28. Find the Index of the First Occurrence in a String

# haystack  = input("Enter haystack: ")
# needle = input("Enter needle: ")
# if needle in haystack:
#             result = haystack.index(needle)
#             print(result)
# else:
#     print(-1)
    

# 125. Valid Palindrome

# s = input("Enter a string: ")
    
# # convert all the characters in lowercase
# s = s.lower()
# res = ""

# for ch in s:
#     # alnum only include digit and no. remove non alphanumeric character like space , ; : etc
#     if ch.isalnum():
#         res += ch
            
# print(res[:] == res[::-1])