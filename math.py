# Q1
# Example 1:
# Input: n = 4

# Output: 1

# Explanation: There is only 1 digit in 4.

# Example 2:
# Input: n = 14

# Output: 2

# Explanation: There are 2 digits in 14.

# n = int(input("Enter Number:-"))

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

# other approach
# rn = 0

# while n > 0:
#     digit = n % 10
#     n = n // 10
#     rn = (rn * 10) + digit
# print(rn)

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

# count = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
        
# if count == 2:
#     print("true")
# else:
#     print("false")

# 790. Count of Prime Numbers till N
# You are given an integer n. You need to find out the number of prime numbers in the range [1, n] (inclusive). Return the number of prime numbers in the range.

# A prime number is a number which has no divisors except, 1 and itself.

# Example 1:
# Input: n = 6

# Output: 3

# Explanation: Prime numbers in the range [1, 6] are 2, 3, 5.

# Example 2:
# Input: n = 10

# Output: 4

# Explanation: Prime numbers in the range [1, 10] are 2, 3, 5, 7.


# count = 0


# for i in range(2, n+1):
    
#     divisor = 0
    
#     for j in range(1, i+1):
#         if i % j == 0:
#             divisor += 1
        
#     if divisor == 2:
#         count += 1
        
# print(count)
        
        
# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.

# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

# Example 1:
# Input: n1 = 4, n2 = 6

# Output: 2

# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

# Greatest Common divisor = 2.

# Example 2:
# Input: n1 = 9, n2 = 8

# Output: 1

# Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.

# Greatest Common divisor = 1.

# n1 = int(input("Enter a number1 :- "))
# n2 = int(input("Enter a number2 :- "))

# l1 = set()
# l2 = set()

# for i in range(1, n1 + 1):
#     if n1 % i == 0:
#         l1.add(i)

# for j in range(1, n2 + 1):
#     if n2 % j == 0:
#         l2.add(j)
        
# c = l1 & l2
# print(len(c))


# You are given two integers n1 and n2. You need find the Lowest Common Multiple (LCM) of the two given numbers. Return the LCM of the two numbers.

# The Lowest Common Multiple (LCM) of two integers is the lowest positive integer that is divisible by both the integers.

# Example 1:
# Input: n1 = 4, n2 = 6

# Output: 12

# Explanation: 4 * 3 = 12, 6 * 2 = 12.

# 12 is the lowest integer that is divisible both 4 and 6.

# Example 2:
# Input: n1 = 3, n2 = 5

# Output: 15

# Explanation: 3 * 5 = 15, 5 * 3 = 15.

# 15 is the lowest integer that is divisible both 3 and 5.

# n3 = n1 * n2
# l = []
# for i in range(1, n3+1):
#     if i % n1 == 0 and i % n2 == 0:
#         l.append(i)
        
# print(min(l))

# divisor = 0
# l = []
# for i in range(1,n+1):
    
#     if n % i == 0:
#         divisor += 1
#         l.append(i)
    
# print(l)

s = input("Enter String = ")
for i in range(1):
    print(s[::-1])