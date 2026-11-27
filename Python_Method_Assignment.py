# Section A: String Methods

# 1 Take s = "python programming". Use upper(), lower(), title(), capitalize() and swapcase() and print the result of each.

# s = "python programming"

# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())
# print(s.swapcase())

# 2 For s = "Programming", print the length using len(), the first character, the last character, s[0:4], s[-3:] and s[::2].

# s = "Programming"
 
# print(len(s))
# print(s[0])
# print(s[-1])
# print(s[0:4])
# print(s[-3:])
# print(s[::2])


# 3 Reverse the string "Python" using slicing and print it.

# s = "Python"

# print(s[::-1])

# 4 Use strip(), lstrip() and rstrip() on the string " hello ". Print the length before and after using len().

# s =  " hello "
# print(len(s))
# print(s.strip())

# print(s.lstrip())

# print(s.rstrip())


# 5 Use replace() to change every "a" to "@" in "banana". Then replace only the first 2 occurrences using the count argument.

# s = "banana"

# print(s.replace("a","@"))

# print(s.replace("a","@",2))

# Use split() on "apple,banana,mango" with a comma. Then split the sentence "I love Python programming" by spaces and count the number of words.

# s = "apple,banana,mango"

# print(s.split(","))

# s = "I love Python programming" 
# print(s.split(" "))
# print(len(s.split(" ")))

# 7 Use join() to join the list ["Python", "is", "easy"] with a space, and then with a hyphen.

# l = ["Python", "is", "easy"]


# print(" ".join(l))
# print("-".join(l))


# 8 Use find() and index() to search for "o" in "hello world". What do both return when the character is not present? Also use rfind() to get the last position of "o".

# s = "hello world"

# print(s.find("f"))
# print(s.index("f"))

# if the character is not present then find will return -1 and index will give ValueError: substring not found

# 9 Use count() to count the letter "a" and the substring "an" in "banana".

# s = "banana"

# print(s.count("a"))
# print(s.count("an"))

# 10 Use startswith() and endswith() to check if the filename "report.pdf" ends with ".pdf" and starts with "rep".

# name = "report.pdf"

# print(name.startswith("rep"))
# print(name.endswith(".pdf"))

# 11 Use isalpha(), isdigit(), isalnum() and isspace() on these strings and print the results: a = "Python" b = "12345" c = "Python3" d = "   "

# a = "Python"
# b = "12345"
# c = "Python3" 
# d = "   "

# print(a.isalpha())
# print(b.isdigit())
# print(c.isalnum())
# print(d.isspace())

# 12 Use isupper() and islower() on "HELLO", "hello" and "Hello".



# s = "HELLO"
# s = "hello"
# s = "Hello"

# print(s.isupper())
# print(s.islower())


# 13 Use center() to place "Hi" in the middle of width 10 using "*". Use zfill() to make "42" a 5 digit number like 00042.
# s = "Hi"
# print(s.center(10,"*"))

# s = "42"
# print(s.zfill(5))

# Use partition() on "name=Riya" with "=" and print the three parts. Use splitlines() on a string that has two lines.

# s = "name=Riya"

# print(s.partition("="))
# s = "Hello Kanishak\nGood morning"
# print(s.splitlines())



# 15 Print My name is Riya and I am 20 years old using format() and then using an f-string, with the variables name and age.

# name = "Riya"
# age = 22
# print(f"My name is {name} and I am {age} year old".format(name,age))

# 16 Try to change the first letter of s = "hello" using s[0] = "J". Write the error and explain why strings are immutable. Then show the correct way to get "Jello".

# s = "hello"


# s[0] = "J"

# print(s)
# String is immuatable so this will give TypeError: 'str' object does not support item assignment
# print(s.replace(s[0], "J"))

# Section B: String Coding Practice (Interview Questions)

# 17 Write a program to check whether a string is a palindrome (for example madam, level).

# s = "madam"

# if s[:] == s[::-1]:
#     print("s is palindrome")
    
# else:
#     print("not palindrome")

# 18 Count the number of vowels and consonants in a string entered by the user.
# s = input("Enter string = ")

# vowel_count = 0
# consonant_count = 0

# for ch in s:
#     if ch.lower() in "aeiou":
#         vowel_count += 1
        
#     else:
#         consonant_count += 1
      
        
# print("Vowel count is = ", vowel_count)
# print("Consonants count is = ", consonant_count)

# 19 Check whether two strings are anagrams of each other (for example listen and silent).

# s = input("Enter string = ")
# s1 = input("Enter string1 = ")

# l = list(s)
# l.sort()

# l1 = list(s1)
# l1.sort()

# if l == l1:
#     print("s1 and s is anargam")
# else:
#     print("not anargam")

# 20 Reverse each word of a sentence but keep the word order the same. Example: hello world becomes olleh dlrow.

s = "hello world"

t = s.split(" ")
print(t[::-1])
