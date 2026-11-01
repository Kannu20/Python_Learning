# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print("Car started")


# c1 = Car("BMW", "Black")
# c2 = Car("Audi", "White")

# print(c1.brand,",",c1.color)
# print(c2.color)

# c1.start()


# class Employee:
#     def __init__(self):
#         self.eid = 123
#         self.ename = 'Om'
#         self.ecity = 'Goa'
        
#     def display(self):
#         print("employee id is: ", self.eid)
#         print("employee name is: ", self.ename)
#         print("employee city is: ", self.ecity)
    
# e = Employee()

# e.display()

# class Employee:
#     def __init__(self):
#         self.eid = int(input("Enter eid: "))
#         self.ename = input("Enter ename: ")
#         self.eage = int(input("Enter eage: "))
        
#     def display(self):
#         print("Enter eid: ", self.eid)
#         print("Enter ename: ", self.ename)
#         print("Enter eage: ", self.eage)
        
# e1 = Employee()
# e2 = Employee()

# print()

# print("Employee Details Are: ")

# e1.display()
# e2.display()

# With Multiple Parameters
# class Employee:
#     def __init__(self, eid , ename, eage):
#         self.eid = eid
#         self.ename = ename
#         self.eage = eage
        
#     def display(self):
#         print("Enter eid: ", self.eid)
#         print("Enter ename: ", self.ename)
#         print("Enter eage: ", self.eage)
        
# e1 = Employee(eid = 123, ename = "kannu", eage= 21)
# e2 = Employee(eid = 124, ename = "kanishak", eage= 22)

# print()
# print("Employee Details Are: ")
# print()
# e1.display()
# print()
# e2.display()

# print(e1.__dict__)

# Instance Variable

# class Test:
#     def __init__(self):
#         self.a = 10
    
#     def m1(self):
#         self.b = 20
        
# t = Test()

# t.c = 9

# print(t.__dict__) # Here b = 30 is not print because here we don't call m1 so that's why the value of b is not executed

# t.m1()
# print(t.__dict__)

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20 
        
#     def m1(self):
#         print("inside the class")
        
#         print(self.a)
#         print(self.b)

# t = Test()

# t.m1()
# print("outside of the class")
# print(t.a)
# print(t.b)

# class test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
        
#     def m1(self):
#         del self.b # Delete the instance variable with in the class
        
# t1 = test()
# t2 = test()


# t1.m1()
# print("t1 = ", t1.__dict__)
# print("t2 = ", t2.__dict__)

# del t2.a
# print("t2 after deleting a element = ", t2.__dict__)


# Local Variable
class Test:
    def m1(self):
        a = 10
        print(a)
        
    def m2(self):
        b = 20
        print(b)
        # print(a) pp# Here a is not defined because a is local variable and it is only accessible in m1 method
        
t = Test()
t.m1()
t.m2()