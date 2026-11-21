
# Name: Kanishak Todwal Date: 21/10/26

# Section A: Function Basics (define, call, print, return)




# 1 Write a function greet() that prints Hello, Welcome to Python! Call it 3 times.
# n = int(input("Enter n = "))
# def greet(n):
#     for i in range(n):
#         print("Hello, Welcome to Python!")
# greet(n)

# 2 Write a function add(a, b) that prints the sum of two numbers. Call it with the values 10 and 20.

# def add(a, b):
#     print("Sum of a and b is:",a+b)
# add(10, 20)

# 3 Write a function multiply(a, b) that returns the product of two numbers. Store the result in a variable and print it.

# def multiply(a,b):
#     c =  a*b
#     print("product of 2 no. is", c)
#     return c
# multiply(10, 20)

# Write a function square(n) that returns the square of a number. Print square(5) and square(12).
# n = int(input("enter a no. = "))
# def square(n):
#     return n*n

# print("square of", n, "is", square(n))

# Write a function is_even(n) that returns True if the number is even, otherwise False.
# n = int(input("Enter no. = "))
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(n))

# 6 Look at these two functions and say what each one outputs. Explain the difference between print and return.
# def f1(x):
#     print(x * 2)
# def f2(x):
#     return x * 2 
# a = f1(5) 
# b = f2(5) 
# print(a) 
# print(b)

# Ans = return is used to store and save the value in variable and it is reusable in further operation it will automatically call when the function call.
# and Print never store the value it will used to display the value


# 7 Write a function max_of_three(a, b, c) that returns the largest of three numbers without using the built-in max().
# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# c = int(input("Enter c = "))
# def max_of_three(a, b, c):
#     if a > b:
#         return "a is largest"
    
#     elif b > c:
#         return "b is largest"
#     elif a == b == c:
#         return "all no. are equal"
#     else:
#         return "c is largest"
    
# print(max_of_three(a, b, c))