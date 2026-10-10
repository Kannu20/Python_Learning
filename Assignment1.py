#KANISHAK TODWAL ASSIGNMENT SOLUTION
# # Python Practice Questions

# ## Conditional Statements, Operators, Membership, Indexing & Slicing

# ### 1. Positive, Negative, or Zero

# Take a number from the user.

# Check the number:

# * If it is greater than `0`, print `"Positive Number"`.
# * If it is less than `0`, print `"Negative Number"`.
# * If it is equal to `0`, print `"Zero"`.

# sol
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive Number")
# elif num < 0:
#     print("Negative Number")
# else:
#     print("Zero")

# **Use:** `if-elif-else`, relational operators

# ### 2. Even or Odd

# Take an integer from the user.

# Check whether the number is:

# * Even → print `"Even Number"`.
# * Odd → print `"Odd Number"`.

# **Hint:** Use the `%` operator.

# **Use:** Arithmetic operator, `if-else`

# Sol.

# num = int(input("Enter an integer: "))

# if num % 2 == 0:
#     print(num,"Is Even Number")
# else:
#     print(num,"Is Odd Number")


# ### 3. Voting Eligibility

# Take the user's age as input.

# * If the age is `18` or more, print `"Eligible for Voting"`.
# * Otherwise, print `"Not Eligible for Voting"`.

# **Use:** `if-else`, `>=`

# age = int(input("Enter Your Age: "))

# if age > 18:
#     print("Eligible for Voting")
    
# else:
#     print("Not Eligible for Voting")


# ### 4. Greater Number

# Take two numbers from the user.

# Compare both numbers:

# * If the first number is greater, print `"First number is greater"`.
# * If the second number is greater, print `"Second number is greater"`.
# * If both numbers are equal, print `"Both numbers are equal"`.

# **Use:** `if-elif-else`, `>`, `<`, `==`

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# if num1 > num2:
#     print(num1, "First number is greater")
# else:
#     if num2 > num1:
#         print(num2, "Second number is greater") 
#     else:
#         print(num1, "Both numbers are equal", num2)

# ### 5. Divisible by 5 and 10

# Take an integer from the user.

# Check:

# * If the number is divisible by both `5` and `10`, print `"Divisible by both 5 and 10"`.
# * If it is divisible only by `5`, print `"Divisible by 5"`.
# * Otherwise, print `"Not divisible by 5 or 10"`.

# **Use:** `%`, `and`, `if-elif-else`

# sol

# num = int(input("Enter an integer: "))

# if num % 5 == 0 and num % 10 == 0:
#     print(num,"Is Divisible by both 5 and 10")
    
# elif num % 5 == 0:
#     print(num,"Is Divisible by 5")
    
# else:
#     print("Not divisible by 5 or 10")

# ### 6. Number in Range

# Take a number from the user.

# Check whether the number is between `10` and `50`.

# * If yes, print `"Number is in range"`.
# * Otherwise, print `"Number is out of range"`.

# **Use:** `and`, `>=`, `<=`

# num = int(input("Enter Number: "))


# if num >= 10 and num <= 51:
#     print(num, "Is in range b/w 10 and 50")
    
# else:
#     print(num, "is out of range")

# ### 7. Check Vowel

# Create the following string:

# ```python
# vowels = "aeiou"
# ```

# Take one character from the user.

# Check whether the character is present in `vowels`.

# * If present, print `"It is a vowel"`.
# * Otherwise, print `"It is not a vowel"`.

# **Use:** `in`

# chr1 = input("Enter character: ")

# vowels = ['a','e','i','o','u']

# if chr1 in vowels:
#     print(chr1, "is vowel")
    
# else:
#     print(chr1, "is not vowel")

# ### 8. Check Digit

# Create the following string:

# ```python
# digits = "0123456789"
# ```

# Take one character from the user.

# Check whether the character is not present in `digits`.

# * If it is not present, print `"It is not a digit"`.
# * Otherwise, print `"It is a digit"`.

# **Use:** `not in`

# chr1 = input("Enter character: ")

# digits = ['0','1','2','3','4','5','6','7','8','9']

# if chr1 not in digits:
#     print("It is not a digit")
    
# else:
#     print("It is a digit")

# ### 9. Check Student Name

# Create the following list:

# ```python
# students = ["Anil", "Gaurav", "Ayush", "Nitin", "Rohit"]
# ```

# Take a student name from the user.

# Check whether the name is present in the list.

# * If present, print `"Student is present"`.
# * Otherwise, print `"Student is not present"`.

# **Use:** `in`
# sol

# name = input("Enter name: ")

# students = ["Anil", "Gaurav", "Ayush", "Nitin", "Rohit"]

# if name in students:
#     print(name, "is present")
# else:
#     print(name,"is not present")

# ### 10. Check Restricted Word

# Create the following list:

# ```python
# restricted_words = ["spam", "scam", "fake"]
# ```

# Take a word from the user.

# * If the word is present in the list, print `"This word is restricted"`.
# * Otherwise, print `"This word is allowed"`.

# **Use:** `in`, `not in`

# word = input("Enter the word: ")

# restricted_words = ["spam", "scam", "fake"]

# if word in restricted_words:
#     print("This word is restricted")
    
# else:
#     print("This word is allowed")
    
# ### 11. Grade Calculator

# Take the student's marks as input.

# Print the grade according to these rules:

# ```text
# 90–100   → A
# 80–89    → B
# 70–79    → C
# 60–69    → D
# Below 60 → Fail
# ```

# If the marks are greater than `100` or less than `0`, print `"Invalid Marks"`.

# **Use:** `if-elif-else`, relational operators

# marks = int(input("Enter student marks: "))

# if marks >= 90 and marks <= 100:
#     print("Grade is A")
    
# elif marks >= 80 and marks <= 89:
#     print("Grade is B")

# elif marks >= 70 and marks <= 79:
#     print("Grade  is C")
    
# elif marks >= 60 and marks <= 69:
#     print("Grade is D")
    
# elif marks > 100 and marks < 0:
#     print("Invaild Marks")
    
# else:
#     print("Fail")


# ### 12. Temperature Checker

# Take the temperature as input.

# Print the appropriate message:

# ```text
# Above 40 → Very Hot
# 30–40    → Hot
# 20–29    → Normal
# Below 20 → Cold
# ```

# **Use:** `if-elif-else`

# temp = int(input("Enter temprature in celcius: "))

# if temp > 40:
#     print("very hot")
# elif temp <= 40 and temp >= 30:
#     print("Hot")
# elif temp <= 29 and temp >= 20:
#     print("Normal")
# else:
#     print("Cold")

# ### 13. Simple Calculator

# Take the following inputs from the user:

# * First number
# * Second number
# * Operator

# The operator can be:

# ```text
# +
# -
# *
# /
# ```


# Perform the appropriate calculation based on the operator.

# If the user enters another operator, print `"Invalid Operator"`.


# **Use:** `if-elif-else`, arithmetic operators

#sol
# num1 = float(input("Enter 1st No. = "))
# num2 = float(input("Enter 2nd No. = "))

# operator = input("Enter operator: ")

# if operator == '+':
#     print(num1 + num2)
    
# elif operator == '-':
#     print(num1 - num2)
    
# elif operator == '*':
#     print(num1 * num2)

# elif operator == '/':
#     print(num1 / num2)
    
# else:
#     print("Invalid Opertor")


# ### 14. Divisible by 3 and 5

# Take a number from the user.

# Check:

# * If the number is divisible by both `3` and `5`, print `"Divisible by both"`.
# * If it is divisible only by `3`, print `"Divisible by 3"`.
# * If it is divisible only by `5`, print `"Divisible by 5"`.
# * If it is not divisible by either, print `"Not divisible by 3 or 5"`.

# **Use:** `%`, `and`, `if-elif-else`

# sol
# num = int(input("Enter an number: "))

# if num % 5 == 0 and num % 3 == 0:
#     print(num,"Is Divisible by both 5 and 3")
    
# elif num % 3 == 0:
#     print(num,"Is Divisible by 3")
    
# elif num % 5 == 0:
#     print(num,"Is Divisible by 5")
    
# else:
#     print("Not divisible by 5 or 3")


# ### 15. Age Category

# Take the age as input.

# Print the category according to these rules:

# ```text
# 0–12  → Child
# 13–19 → Teenager
# 20–59 → Adult
# 60+   → Senior Citizen
# ```

# If the age is negative, print `"Invalid Age"`.

# sol

# age = int(input("Enter Age: "))

# if age >= 0 and age <= 12:
#     print("CHILD")
    
# elif age >= 13 and age <= 19:
#     print("TEEANAGER")

# elif age >= 20 and age <= 59:
#     print("ADULT")
    
# else:
#     print("SENIOR CITIZEN")
 
# **Use:** `if-elif-else`

# ### 16. Login System

# Create the following variables:

# ```python
# correct_username = "admin"
# correct_password = "1234"
# ```

# Take the username and password from the user.

# Perform the following checks:

# 1. First, check whether the username is correct.
# 2. If the username is correct, check the password.
# 3. If both are correct, print `"Login Successful"`.
# 4. If the username is correct but the password is wrong, print `"Incorrect Password"`.
# 5. If the username is wrong, print `"Incorrect Username"`.

# **Use:** Nested `if`

# sol

# username = input("Enter your username: ")
# password = int(input("Enter your password: "))

# correct_username = "admin"
# correct_password = 1234

# if username == correct_username:
#     if password == correct_password:
#         print("Login Successful")
#     else:
#         print("password is incorrect")
# else:
#     print("username is incorrect")

# ### 17. ATM Withdrawal

# Take the following inputs from the user:

# * Account balance
# * Withdrawal amount

# Perform these checks:

# 1. Check whether the withdrawal amount is greater than `0`.
# 2. If the amount is valid, check whether enough balance is available.
# 3. If enough balance is available, print `"Withdrawal Successful"`.
# 4. If the balance is not enough, print `"Insufficient Balance"`.
# 5. If the withdrawal amount is `0` or negative, print `"Invalid Amount"`.

# **Use:** Nested `if`, relational operators

# sol

# balance = int(input("Enter account balance: "))
# withdraw = int(input("Enter withdraw amount: "))

# if withdraw > 0:
#     # if withdraw > 0 and balance > 0:
#     if withdraw < balance:
#         print("withdraw successful")
#     else:
#         print("withdraw amount greater than balance withdraw not possible")
# elif balance <= 0:
#         print("Insufficient balance")
# else:
#     print("Invalid Amount")
    
        
    

# ### 18. Student Result

# Take the following inputs from the user:

# * Student marks
# * Attendance percentage

# Follow these rules:

# 1. First, check whether attendance is `75%` or more.
# 2. If attendance is sufficient, check the marks.
# 3. If marks are `40` or more, print `"Pass"`.
# 4. If marks are below `40`, print `"Fail"`.
# 5. If attendance is below `75%`, print `"Not Eligible due to Low Attendance"`.

# **Use:** Nested `if`, relational operators

# sol

# marks = int(input("Enter marks: "))
# percentage = float(input("Enter percentage: "))

# if percentage > 75:
#     if marks > 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible due to Low Attendance")

# ### 19. Shopping Discount

# Take the shopping amount from the user.

# Apply the discount according to these rules:

# ```text
# ₹5000 or more → 20% discount
# ₹3000–₹4999  → 15% discount
# ₹1000–₹2999  → 10% discount
# Below ₹1000   → No discount
# ```

# Calculate and print:

# * Discount amount
# * Final amount after discount

# **Use:** `if-elif-else`, arithmetic operators

# shopping_amount = float(input("Enter amount: "))

# if shopping_amount >= 5000:
#     discount = shopping_amount * 0.20
#     print("20% discount applied")

# elif shopping_amount <= 4999 and shopping_amount >= 3000:
#     discount = shopping_amount * 0.15
#     print("15% discount applied")

# elif shopping_amount <= 2999 and shopping_amount >= 1000:
#     discount = shopping_amount * 0.10
#     print("10% discount applied")

# else:
#     discount = 0
#     print("No discount")

# final_amount = shopping_amount - discount

# print("Discount amount:", discount)
# print("Final amount:", final_amount)

# ### 20. Username Validation

# Create the following list:

# ```python
# existing_users = ["rajat", "anil", "gaurav", "rohit"]
# ```

# Take a username from the user.

# * If the username is already present in the list, print `"Username already exists"`.
# * If the username is not present in the list, print `"Username is available"`.

# **Compulsory:** Use `in` or `not in`.

# username = input("Enter Username: ")

# existing_users = ["rajat", "anil", "gaurav", "rohit"]

# if username in existing_users:
#     print("Username already exists")
# else:
#     print("Username is available")

# ### 21. Add Value Using `+=`

# Start with:

# ```python
# x = 10
# ```

# Add `5` to `x` using the `+=` assignment operator.

# Print the updated value.

# **Expected output:**

# ```text
# 15
# ```

# x = 10

# x += 5

# print("Updated Value is: "x)



# ### 22. Subtract Value Using `-=`

# Start with:

# ```python
# balance = 1000
# ```

# Subtract `250` from `balance` using the `-=` assignment operator.

# Print the updated balance.

# **Expected output:**

# ```text
# 750
# ```

# balance = 1000

# balance -= 250

# print("Updated balance is: ",balance)

# ### 23. Calculate Total Marks

# Start with:

# ```python
# total = 0
# ```

# Take marks for three subjects from the user.

# Add all three marks to `total` using the `+=` operator.

# Finally, print the total marks.

# **Example:**

# ```text
# Maths: 80
# Python: 90
# English: 70

# Total = 240
# ```
# **Use:** `+=`

# sol
# marks1 = int(input("marks of subject1: "))
# marks2 = int(input("marks of subject2: "))
# marks3 = int(input("marks of subject3: "))

# total = 0

# total += marks1
# total += marks2
# total += marks3
# print(total)


# ### 24. Shopping Cart Update

# Start with:

# ```python
# total = 500
# ```

# Perform the following steps:

# 1. Add another product worth `250`.
# 2. Apply a discount of `100`.
# 3. Use assignment operators to update the total.
# 4. Print the final amount.

# **Use:** `+=`, `-=`

# total = 500

# total += 250
# total -= 100

# print(total)
# ### 25. Update and Compare

# Start with:

# ```python
# number = 10
# ```

# Perform the following steps:

# 1. Add `5` to `number` using `+=`.
# 2. Check whether the updated number is equal to `15`.
# 3. If yes, print `"Correct"`.
# 4. Otherwise, print `"Incorrect"`.

# **Use:** `+=`, `==`, `if-else`

# sol

# number = 10

# number += 5

# if number == 15:
#     print("Correct")
    
# else:
#     print("Incorrect")


### 26. Bank Balance Check

# Start with:

# ```python
# balance = 5000
# ```

# Take the withdrawal amount from the user.

# Perform the following steps:

# 1. Subtract the withdrawal amount from `balance` using `-=`.
# 2. Check whether the updated balance is greater than or equal to `0`.
# 3. If yes, print `"Transaction Successful"`.
# 4. Otherwise, print `"Insufficient Balance"`.

# **Use:** `-=`, `>=`, `if-else`

# balance = 5000

# withdraw = int(input("Enter withdraw amount: "))

# balance -= withdraw

# if balance >= 0:
#     print("Transaction Successful")
    
# else:
#     print("Insufficient Balance")
# ### 27. Check Email

# Take an email address from the user.

# Check whether `"@"` is present in the email.

# * If present, print `"Valid Email Format"`.
# * If not present, print `"Invalid Email Format"`.

# email = input("Enter Your Mail: ")

# if '@' in email:
#     print("Valid Email Format")
    
# else:
#     print("Invalid Email Format")

# **Use:** `in`, `if-else`

# ### 28. Check Password

# Take a password from the user.

# Check whether the password is `"admin"`.

# * If the password is `"admin"`, print `"Weak Password"`.
# * Otherwise, print `"Password Accepted"`.

# **Use:** `!=` or `not in`, `if-else`

# password = input("Enter your password: ")

# current_password = "admin"

# if password != current_password:
#     print("Password Accepted")
    
# else:
#     print("Weak Password")
    

# ### 29. Check Available Fruit

# Create the following list:

# ```python
# fruits = ["apple", "banana", "mango", "orange"]
# ```

# Take a fruit name from the user.

# * If the fruit is present in the list, print `"Fruit is available"`.
# * Otherwise, print `"Fruit is not available"`.

# **Compulsory:** Use the `in` operator
# sol

# fruits = ["apple", "banana", "mango", "orange"]

# name = input("Enter fruit name: ")

# if name in fruits:
#     print("Fruit is available")

# else:
#     print("Fruit is not available")

# ### 30. Number Guessing

# Create the following variable:

# ```python
# secret_number = 50
# ```

# Take a number from the user.

# Check:

# * If the number is equal to `50`, print `"Correct Guess"`.
# * If the number is greater than `50`, print `"Too High"`.
# * If the number is less than `50`, print `"Too Low"`.

# **Use:** `if-elif-else`, relational operators, type casting

# secret_number = 50

# user_number = int(input("Enter Your Number: "))

# if user_number == secret_number:
#     print("Correct Guess")

# elif user_number > secret_number:
#     print("Too high")
    
# else:
#     print("Too low")
# # Indexing and Slicing Practice

# ### 31. Get the First Character

# Take a string from the user.

# Print the first character of the string using indexing.

# **Example:**

# ```text
# Input: Python
# Output: P
# ```

# **Use:** String indexing

# chr1 = input("Enter Character: ")

# print(chr1[0])

# ### 32. Get the Last Character

# Take a string from the user.

# Print the last character of the string using negative indexing.

# **Example:**

# ```text
# Input: Python
# Output: n
# ```

# chr1 = input("Enter Character: ")

# print(chr1[-1])

# **Use:** Negative indexing

# ### 33. Get Specific Characters

# Take a string from the user.

# Print:

# * The first character
# * The third character
# * The last character

# Use indexing to access each character.

# **Example:**

# ```text
# Input: Python

# Output:
# P
# t
# n
# ```


# **Use:** Positive and negative indexing

# str1 = input("Enter the string: ")

# print("1st Character:",str1[0])
# print("2nd Character:",str1[2])
# print("3rd Character:",str1[-1])
# ### 34. Reverse a String

# Take a string from the user.

# Reverse the complete string using slicing.

# **Example:**

# ```text
# Input: Python
# Output: nohtyP
# ```

# **Use:** Slicing, negative step

# str1 = input("Enter the string: ")

# print(str1[::-1])

# ### 35. Print the First Five Characters

# Take a string from the user.

# Print only the first five characters using slicing.

# **Example:**

# ```text
# Input: Programming
# Output: Progr
# ```

# **Use:** String slicing

# str1 = input("Enter the string: ")

# print("First five character are:",str1[0:6])

# ### 36. Print Characters from Index 2 to 6

# Take a string from the user.

# Print the characters starting from index `2` up to, but not including, index `6`.

# **Example:**

# ```text
# Input: PythonProgramming
# Output: thon
# ```

# **Use:** Slicing `[start:stop]`

# str1 = input("Enter the string: ")

# print(str1[2:6])

# ### 37. Print Every Second Character

# Take a string from the user.

# Print every second character using slicing.

# **Example:**

# ```text
# Input: Python
# Output: Pto
# ```

# **Use:** Slicing with step `[::2]`

# str1 = input("Enter the string: ")

# print(str1[::2])



# ### 38. Check First and Last Character

# Take a string from the user.

# Check whether the first and last characters are the same.

# * If they are the same, print `"First and last characters are same"`.
# * Otherwise, print `"First and last characters are different"`.

# **Use:** Indexing + `if-else`

# str1 = input("Enter the string: ")

# if str1[0] == str1[-1]:
#     print("First and last characters are same")
    
# else:
#     print("First and last characters are different")

# ### 39. Check Vowel at First Position

# Take a word from the user.

# Use indexing to get the first character.

# Check whether the first character is present in:

# ```python
# vowels = "aeiou"
# ```

# * If present, print `"The word starts with a vowel"`.
# * Otherwise, print `"The word does not start with a vowel"`.

# **Use:** Indexing + `in` + `if-else`

# word = input("Enter word: ")

# vowels = "aeiou"

# if word[0] in vowels:
#     print("The word starts with a vowel")
    
# else:
#     print("The word does not start with a vowel")

# ### 40. Extract Username from Email

# Take an email address from the user.

# **Example:**

# ```text
# Input:
# rajat@gmail.com
# ```

# Extract and print only the username.

# **Expected output:**

# ```text
# rajat
# ```

# **Hint:** Find the position of `"@"` and use slicing.

# **Use:** String indexing/slicing, `in`, and string methods

email = input("Enter your email: ")

position = email.index("@")  
username = email[:position]
print(username)