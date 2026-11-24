
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

# Section B: Local and Global Variables

# 8 Write a program with a global variable name = "Ravi". Create a function that prints this global variable and call it.

# name = "Ravi" #global variable

# def main():
#     print(name)
# main()

# 9 What will be the output of this code? Why does the error occur?
# def show():    
#     x = 50    
#     print(x) 
# show()
# print(x)

# ans = this code will give the output 50 first after that NameError: name 'x' is not defined for the print that we call after show() because we define x inside the function so we can not access it outside the function because it is local variable for the particular fuction show()

# 10 Create a function with a local variable city = "Jaipur" and print it inside the function. Then try printing it outside and write in a comment why it fails.

# def main():
#     city = "Jaipur"
#     print(city)
# main()
# print(city)

# It will fails because we make the city as a local variable in the function main and if we try to call this local varible outside of the function then it will give NameError

# Predict the output (local variable priority):
# x = 100 
# def test():    
#     x = 10
#     print("Inside:", x) 
# test()
# print("Outside:", x)

# For inside it print 10 print if we declare local variable in a function then it will give first priority to local variable so that's why inside print 10 and outside print 100 because it will print outside of the function if any local variable not assign then it will always print global variable

# Using the same variable name value = 5 as both global and local, write a program that proves the local variable gets priority inside the function.

# value = 5 # global variable

# def main():
#     value = 6 # local variable
    
#     print("local variable: ",value)
    
# main()

# here both variable of local and global are same but here 1st priority is given to local variable

# Using globals(), write a function that has a local variable a = 20 and a global variable a = 99. Print both values from inside the function.

# Using globals(), write a function that has a local variable a = 20 and a global variable a = 99. Print both values from inside the function.

# a = 99

# def main():
#     a = 20
#     print("local variable =",a)
    
#     print("global variable =",globals()['a'])
    
# main()

# 14 Write a function increase() that uses the global keyword to add 10 to a global variable count = 0. Call it 3 times and print count.

# count = 0
# def increase():
#     global count
#     count += 10
# increase()
# increase()
# increase()
# print(count)
    
# 15 Create a global variable balance = 1000. Write two functions, deposit(amount) and withdraw(amount), that modify the global balance. Show the balance after a few operations.

# balance = 1000

# def deposit(amount):
#     global balance
#     balance += amount
#     print('Your deposited amount is = ', amount)
#     print('Your updated amount is = ', balance)
    
# deposit(2000)

# def withdraw(amount):
#     global balance
#     balance -= amount
#     print('Your withdraw amount is = ', amount)
#     print('Your updated amount is = ', balance)
    
# withdraw(500)

# Section C: Types of Arguments

# 16 (Positional arguments) Write a function student_info(name, age, course) that prints the details. Call it with positional arguments. Then change the order of the arguments and observe what happens.

# def student_info(name, age, course):
#     print("student name is = ",name)
#     print("student age is = ",age)
#     print("student course is = ",course)
    
# student_info("kanishak",21,"Python")
# student_info(21,"Python", "Kannu")
# student_info("Python",21, "Kannu")

# if we change the order of the arguments then it will impact on our ans it will change the ans

# 17 (Keyword arguments) Call the same student_info() function using keyword arguments in a different order. Does the output stay correct?

# def student_info(name, age, course):
#     print("My name is",name,"age is",age,"course is",course)
    
# student_info(name = "kanishak",age = 21,course= "python")
# student_info(course = "Python",age = 21,name= "kanishak")
# student_info(age = 22,name = "kannu",course= "c")

# here order is different but output is same because here we define keyword and parameter so it will not impact on the order

# 18 (Default arguments) Write a function power(base, exp=2) that returns base ** exp. Call it with one argument, and then with two arguments.

# def power(base, exp = 2):
#     return base**exp

# print(power(3))
# print(power(4,4))
# print(power(5))


# 19 Write a function introduce(name, country="India") that prints My name is <name> and I am from <country>. Call it in 3 ways: only name, name and country by position, and name and country by keyword.

# def introduce(name, country="India"):
#     print("My name is", name,"and I am from",country)
    
# introduce("kanishak")
# introduce("kanishak","india")
# introduce(name = "kanishak", country="india")


# 20 (Variable-length *args) Write a function total(*numbers) that returns the sum of any number of arguments. Test it with 2 numbers, 5 numbers, and no numbers.

# def total(*numbers):
#     return sum(numbers)

# print(total(1,2))
# print(total(1,2,3,4,5))
# print(total())

# 21 Write a function average(*nums) that returns the average of all given numbers. If no number is given, return 0.

# nums = tuple(map(int,input("Enter nums = ").split()))
# def average(*nums):
#     if len(nums) == 0:
#         return 0
#     return sum(nums) / len(nums)
    
    
# print(average(*nums))

# 22 (Keyword variable-length **kwargs) Write a function show_details(**info) that prints each key and value. Call it with name="Amit", age=20, city="Delhi".

# def show_details(**info):
#     for K , V in info.items():
#         print(K, "=" , V)
        
# show_details(name = "Amit", age = "20", city = "Delhi")
    
    
# 23 Write a function profile(name, *hobbies, **details) that prints the name, then the hobbies, then the details. Call it with a name, 3 hobbies, and 2 extra details such as age and city.

# def profile(name, *hobbies, **details):
#     print("My name is", name)
#     print("My hobbies are =", hobbies)
    
#     print("My Details")
#     for K, V in details.items():
#         print(K, "=", V)
    

# profile("kanishak","playing","singing","dancing", city="Jaipur", age=22)


# Find the errors in the code below and fix them:

# def demo(a, b=10, c): # here c give error because in python we can't use non default argument after default argument there are 2 correct ways first we can place c before b and 2nd case is we should have to assign some value to c i.e make c as also a default argument
# def demo(a, b = 10, c = 12):
def demo(a, c , b = 10):
    print(a, b, c) 
def info(name, age):
    print(name, age)
# info(age=20, "Riya") # this line give error positional argument follows keyword argument and here we didn't assign the keyword for riya so the correct output is below
info(age = 20, name="Riya")
# info("Riya", 20, 30) # this line give error because info have only 2 arguments and here we pass 3 argument so if we call any function it is compulsory to assign only those argument that are assigned in this particular function

info("Riya", 22)


# Bonus Questions

# 25 Write a function calculator(a, b, operation="add") that returns the result of add, subtract, multiply, or divide depending on operation. Handle division by zero by returning a message.

def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a-b
    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        if b == 0:
            return "Can't divide by 0"
        return a/b
    else:
        return "enter valid input"
    
# print(calculator(10,20))
# print(calculator(10,20,"subtract"))
# print(calculator(10,20,"multiply"))
# print(calculator(10,20,"divide"))
# print(calculator(10,0, "divide"))

# 26 Write a function count_calls() that uses a global variable to count how many times it has been called, and prints the count each time.

n = int(input("Enter value of n that how much time you want to to run the function = "))
count = 0
def count_calls():
    global count
    count += 1
    print(count)

for i in range(n):       
    count_calls()
    
