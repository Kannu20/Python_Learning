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
# class Test:
#     def m1(self):
#         a = 10
#         print(a)
        
#     def m2(self):
#         b = 20
#         print(b)
#         # print(a) # Here a is not defined because a is local variable and it is only accessible in m1 method
        
# t = Test()
# t.m1()
# t.m2()

# Inner Class
# class outer:
    
#     def __init__(self):
#         print("outer class constructor")
        
#     class inner:
        
#         def __init__(self):
#             print("inner class constructor")
#         def m1(self):
#             print("inner class method")
                
# o = outer()
# i = o.inner()
# i.m1()

# i = outer().inner()
# outer().inner().m1()

# import gc

# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())


# import time

# class Test:
#     def __init__(self):
#         print("constructor")
        
#     def __del__(self):
#         print("destructor")
        
# t = Test()
# time.sleep(2)
# print("end")

# class Test:
#     x = 10
#     _y = 20
#     __z = 40
#     def __init__(self):
#         print(self.x)
#         print(self._y)
#         print(self.__z)
        
# t = Test()
# print("Outside of class")
# print(t.x)
# print(t._y)
# print(t.__z) this will give error because it is strongly private we can't access it outside of the class
# Single Inheritence
# class Branch:
#     def get_branch_details(self):
#         self.bcode = int(input("enter bcode: "))
#         self.bname = str(input("enter bname: "))
#         self.baddress = str(input("enter baddress: "))
        
#     def display_detail(self):
#         print("Branch code is: ", self.bcode)
#         print("Branch name is: ", self.bname)
#         print("Branch address is: ", self.baddress)

# class Employee(Branch):
#     def get_emp_details(self):
#         self.eid = int(input("enter eid: "))
#         self.ename = str(input("enter ename: "))
#         self.eaddress = str(input("enter eaddress: "))
        
#     def display_detail_emp(self):
#         print("Emp code is: ", self.eid)
#         print("Emp name is: ", self.ename)
#         print("Emp address is: ", self.eaddress)
        
# e = Employee()
# e.get_branch_details()
# e.get_emp_details()
# e.display_detail()
# e.display_detail_emp()


# class car:
    
#     def __init__(self):
#         self.__updatesoftware()
#     def __updatesoftware(self):
#         print("software is updated")
        
# c = car()
# c.__updatesoftware() # this will give error because it is strongly private

# class car:
#     __name = " "
#     __maxspeed = 0
    
#     def __init__(self):
#         self.__name = "BMW"
#         self.__maxspeed = 200
#         print(self.__name)
#         print(self.__maxspeed)
        
#     def drive(self):
#         print("Drive {} car with maxspeed {}".format(self.__name, self.__maxspeed))
        
#     def set_speed(self, speed):
#         self.__maxspeed = speed
#         print("Driving {} car with the with updated max speed {}".format(self.__name, self.__maxspeed))
# c = car()
# c.drive()

# c.set_speed(300)
# c.drive() # here max speed is updated because we set the max speed 300 in the same class so that's why it will change the speed globally for the particular class

# class branch:
#     def get_branch(self):
#         self.bcode = int(input("enter bcode: "))
#         self.bname = str(input("enter bname: "))
        
#     def display_branch(self):
#         print("Branch code is: ", self.bcode)
#         print("Branch name is: ", self.bname)
        
# class emp(branch):
#     def get_emp(self):
#         self.ename = input("emp name: ")
        
#     def display_name(self):
#         print("name is : ", self.ename)
        
# class salary(emp):
#     def get_emp_salary(self):
#         self.salary = int(input("emp salary: "))
        
#     def display_salary(self):
#         print("salary is: ",self.salary)
        
# s = salary()
# s.get_branch()
# s.get_emp()
# s.get_emp_salary()
# s.display_branch()
# s.display_name()
# s.display_salary()

# Herirchial Inheritence
# class branch:
#     def get_branch(self):
#         self.bcode = int(input("enter bcode: "))
    
        
#     def display_branch(self):
#         print("Branch code is: ", self.bcode)
        
        
# class name(branch):
#     def get_branch_name(self):
#         self.bname = input("branch name: ")
        
#     def display_name(self):
#         print("branch name is : ", self.bname)

# n = name()
# n.get_branch()
# n.get_branch_name()
# n.display_branch()
# n.display_name()
# class loc(branch):
#     def get_branch_loc(self):
#         self.loc = input("branch location: ")
        
#     def display_loc(self):
#         print("location is: ",self.loc)
        
# l = loc()
# l.get_branch()
# l.get_branch_loc()
# l.display_branch()
# l.display_loc()

# print(issubclass(loc, name))
# print(issubclass(name, branch))
# print(issubclass(loc, branch))

# print(isinstance(loc,name))
# print(isinstance(loc,name))

# class A:
#     def __init__(self):
#         print("A class constructor")
        
# class B(A):
#     pass
#     # def __init__(self):
#     #     print("B class constructor")
        
# b = B()
#  Hybrid Inhertence
# class A:
#     def f1(self):
#         print("f1 function of class A")
        
# class B(A):
#     def f2(self):
#         print("f2 function of class B")
        
# class C(A):
#     def f3(self):
#         print("f3 function of class C")
        
# class D(B,C):
#     def f4(self):
#         print("f4 function of class D")
        
# d = D()
# d.f1()
# d.f2()
# d.f3()
# d.f4()

# class Book:
#     def __init__(self, pages):
#         self.pages = pages
        
#     def __add__(self, other):
#         return self.pages + other.pages
    
# b1 = Book(10)
# b2 = Book(20)

# print(b1+b2)

class Test:
    def m1(self):
        print("no argument")     
        
    def m1(self, a):
        print("1 argument")
        
    def m1(self, a, b):
        print("2 argument")
        
t = Test()
t.m1(10)