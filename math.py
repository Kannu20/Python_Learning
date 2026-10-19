# Q1
# Example 1:
# Input: n = 4

# Output: 1

# Explanation: There is only 1 digit in 4.

# Example 2:
# Input: n = 14

# Output: 2

# Explanation: There are 2 digits in 14.

n = int(input("Enter Number:-"))

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

# s = str(n)
# print(s[::-1])

# Example 1:
# Input: n = 121

# Output: true

# Explanation: When read from left to right : 121.

# When read from right to left : 121.

# Example 2:
# Input: n = 123

# Output: false

# Explanation: When read from left to right : 123.

# When read from right to left : 321.

# s = str(n)

# s1 = s[::]
# s2 = s[::-1]

# print(bool(s1 == s2))

# Example 1:
# Input: n = 25

# Output: 5

# Explanation: The largest digit in 25 is 5.

# Example 2:
# Input: n = 99

# Output: 9

# Explanation: The largest digit in 99 is 9.

# largest = 0
# while n > 0:
#     digit = n % 10
    
    
#     if digit > largest:
#         largest = digit
#     n = n // 10
# print(largest)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = n * factorial(n-1)
#         return result
        
# print(factorial(n))

# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

# Example 1:
# Input: n = 153

# Output: true

# Explanation: Number of digits : 3.

# 13 + 53 + 33 = 1 + 125 + 27 = 153.

# Therefore, it is an Armstrong number.

# Example 2:
# Input: n = 12

# Output:
# false

# Explanation: Number of digits : 2.

# 12 + 22 = 1 + 4 = 5.

# Therefore, it is not an Armstrong number.


# original = 0
# digits = len(str(n))
# total = 0


# while n > 0:
#     digits = n % 10
#     total += digits * digits
#     n = n // 10
    
# print(total == original)

# You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.

# A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.

# Example 1:
# Input: n = 6

# Output: true

# Explanation: Proper divisors of 6 are 1, 2, 3.

# 1 + 2 + 3 = 6.

# Example 2:
# Input: n = 4

# Output: false

# Explanation: Proper divisors of 4 are 1, 2.

# 1 + 2 = 3.

# total = 0

# for i in range(1,n):
#     if n % i == 0:
#         total += i
    
# print(total == n)

# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.

# A prime number is a number which has no divisors except 1 and itself.

# Example 1:
# Input: n = 5

# Output: true

# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# Example 2:
# Input: n = 8

# Output: false

# Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

