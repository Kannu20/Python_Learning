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

class Employee:
    def __init__(self):
        self.eid = int(input("Enter eid: "))
        self.ename = input("Enter ename: ")
        self.eage = int(input("Enter eage: "))
        
    def display(self):
        print("Enter eid: ", self.eid)
        print("Enter ename: ", self.ename)
        print("Enter eage: ", self.eage)
        
e = Employee()
print()
print("Employee Details Are: ")
e.display()

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