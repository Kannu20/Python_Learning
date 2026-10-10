# LOOP PRACTICE: 20 SIMPLE QUESTIONS
# Try each question on your own first, then check the hint.


# 1. Print numbers from 1 to 10 using a for loop.
#    (Hint: range(1, 11))

# for i in range(1, 11):
#     print(i)


# 2. Count backwards from 10 to 1 using a for loop.
#    (Hint: range(10, 0, -1))

# for i in range(10, 0, -1):
#     print(i)

# 3. Print all even numbers from 1 to 20 using a for loop.
#    (Hint: range(2, 21, 2))

# for i in range(2, 21, 2):
#     print(i)


# 4. Take a number as input and print its multiplication table
#    in the format 5 x 1 = 5. (Use a for loop)

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)
    
# 5. Find the sum of numbers from 1 to 50.
#    (Hint: start with total = 0, then use total += i inside the loop)

# num = 50
# total = 0

# for i in range(1, num + 1):
#     total += i
# print("Sum of numbers from 1 to 50:", total)

# 6. Print the squares of numbers from 1 to 10 (1, 4, 9, 16...).
#    (Use a for loop)

# num = 10
# for i in range(1, num + 1):
#     square = i ** 2
#     print("Square of", i, "is", square)

# 7. Print each character of the string "Python" on a separate line.
#    (Use a for loop)

# str = "Python"

# for ch in str:
#     print(ch)
    


# 8. Take a string as input and count the number of vowels in it.
#    (Hint: if ch in "aeiou")

# str = input("Enter a string: ")
# vowel_count = 0

# for ch in str:
#     if ch.lower() in "aeiou":
#         vowel_count += 1

# print("Number of vowels in the string:", vowel_count)

# 9. Find the largest number in the list [4, 9, 2, 7]
#    without using max().
#    (Hint: start with big = lst[0])

# a = [4, 9, 2, 7]
# a = list(input("Enter numbers separated by spaces: "))
# big = a[0]
# for num in a:
#     if num > big:
#         big = num
# print("Largest number in the list:", big)

# 10. Print the following pattern using nested for loops:

#     *
#     **
#     ***
#     ****
#     *****





# 11. Print numbers from 1 to 10 using a while loop.


# 12. Count backwards from 10 to 1 using a while loop.


# 13. Print all even numbers from 1 to 20 using a while loop.


# 14. Find the sum of numbers from 1 to 10 using a while loop.


# 15. Take a number as input and print its multiplication table
#     using a while loop.


# 16. Find the sum of the digits of a number (123 -> 6).
#     (Hint: n % 10 gives the last digit, n //= 10 removes it)


# 17. Reverse a number (123 -> 321) using a while loop.


# 18. Keep asking the user for numbers until they enter 0,
#     then print the sum of all the numbers entered.


# 19. Keep asking the user for a password until they enter
#     the correct one ("python123").


# 20. Print the first 10 numbers of the Fibonacci series
#     (0 1 1 2 3 5...).


# TIP: Solve Q1 to Q3 using a while loop as well, so students
# understand the difference between the two loops.