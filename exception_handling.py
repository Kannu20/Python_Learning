# print(age)

# print([10, 20][4])
# d = {2: 12}
# print(d["name"])
# s = 10
# print(s.append(5))

# for i in range:
# print(i)

# try:
#     age = int(input("enter age = "))
#     print("Your age is",age)
# except ValueError as msg:
#     print(msg)

try:
    n = [10, 20, 30]
    print(n[5])
except IndexError:
    print("Invalid index, use correct index range")