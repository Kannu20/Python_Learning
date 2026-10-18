# Q1
# Example 1:
# Input: n = 4

# Output: 1

# Explanation: There is only 1 digit in 4.

# Example 2:
# Input: n = 14

# Output: 2

# Explanation: There are 2 digits in 14.

n = int(input("enter number:-"))

# s = str(n)

# print(len(s))

# Q2

# Example 1:
# Input: n = 5

# Output: 1

# Explanation: 5 is an odd digit.

# Example 2:
# Input: n = 25

# Output: 1

# Explanation: The only odd digit in 25 is 5.

# count = 0

# while n > 0:
#     digit = n % 10
    
#     if digit % 2 != 0:
#         count += 1
        
#     n = n // 10

# print(count)

# Q3

# Example 1:
# Input: n = 25

# Output: 52

# Explanation: Reverse of 25 is 52.

# Example 2:
# Input: n = 123

# Output: 321

# Explanation: Reverse of 123 is 321.

s = str(n)
print(s[::-1])