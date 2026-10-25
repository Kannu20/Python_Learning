class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("Car started")


c1 = Car("BMW", "Black")
c2 = Car("Audi", "White")

print(c1.brand,",",c1.color)
print(c2.color)

c1.start()