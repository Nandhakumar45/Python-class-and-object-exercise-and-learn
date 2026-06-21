"""
#Exercise 1 (Easy):** Create classes `Dog`, `Cat`, `Bird` with a `sound()` method.
#Expected output: Dog barks, Cat meows, Bird chirps.


class Dog:
    def sound(self):
        print(f"Dog barks")

class Cat:

    def sound(self):
        print("Cat meows")

class Bird:

    def sound(self):
        print("Bird chirps")

d1 = Dog()
d1.sound()

d1 = Cat()
d1.sound()

d1 = Bird()
d1.sound()

"""
"""
In Dog.sound(), you used an f-string f"Dog barks" but there's no {} placeholder inside it, 
so the f prefix isn't doing anything — it works the same as "Dog barks". Not wrong, just unnecessary.
You reused the variable name d1 for all three objects (Dog, Cat, Bird). 
This works fine since Python just reassigns d1 each time, but it's a bit confusing to read. 
Cleaner practice would be using different names like d1, c1, b1:

"""
"""
##Exercise 2 (Easy):** Create classes `Apple`, `Banana`, `Orange` with a `color()` method.
##Expected output: Apple is red, Banana is yellow, Orange is orange.

class Apple:
    def color(self):
        print(f"Apple is red")

class Banana:

    def color(self):
        print("Banana is yellow")

class Orange:

    def color(self):
        print("Orange is orange")

A1 = Apple()
A1.color()

B1 = Banana()
B1.color()

O1 = Orange()
O1.color()

"""
"""
##Exercise 3 (Easy):** Create classes `Square`, `Circle`, `Rectangle` with a `perimeter()` method.
##Expected output: Different perimeter calculations for each shape.

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def perimeter(self):
        return 2 * 3.14 * self.radius
        
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

S1 = Square(5)
print(S1.perimeter())

C1 = Circle(5)
print(C1.perimeter())

R1 = Rectangle(6, 4)
print(R1.perimeter())

"""
"""
#**Exercise 4 (Medium):** Create a parent class `Vehicle` with a `speed()` method. Child classes `Car`, `Bike`, `Truck` override it.
#Expected output: Car goes 100 km/h, Bike goes 80 km/h, Truck goes 60 km/h.

#Note: Exactly right! You can't override from one child class to another child class. Overriding only works from a **parent to child** relationship.

class Vehicle:

    def speed(self):
        pass
class Car:
    def __init__(self,car):
        self.car = car

    def speed(self):
        print(f"Car goes {self.car} km/h")
class Bike:
    def __init__(self, Bike):
        self.Bike = Bike

    def speed(self):
        print(f"Bike goes {self.Bike} km/h")

class Truck:
    def __init__(self, Truck):
        self.Truck = Truck

    def speed(self):
        print(f"Truck goes {self.Truck} km/h")

C1 = Car(100)
C1.speed()

b1 = Bike(80)
b1.speed()

T1 = Truck(60)
T1.speed()

"""
"""
#Exercise 5 (Medium):** Create a parent class `Employee` with a `salary()` method. Child classes `Manager`, `Developer`, `Designer` override it with different salaries.
#Expected output: Different salary amounts for each role.

class Employee:

    def salary(self):
        pass
class Manager(Employee):
    def __init__(self,manager):
        self.manager = manager

    def salary(self):
        print(f"Manager salary {self.manager}")

class Developer(Employee):
    def __init__(self, developer):
        self.developer = developer

    def salary(self):
        print(f"Developer salary {self.developer}")

class Designer(Employee):
    def __init__(self, designer):
        self.designer = designer

    def salary(self):
        print(f"Designer salary {self.designer}")

M1 = Manager(100)
M1.salary()

D1 = Developer(80)
D1.salary()

T1 = Designer(60)
T1.salary()

"""

"""
#**Exercise 6 (Medium):** Create classes `Laptop`, `Phone`, `Tablet` with a `battery_life()` method.
#Expected output: Different battery hours for each device.


class Laptop:
    def battery_life(self):
        print("The battery life is 20%")
class Phone:
    def battery_life(self):
        print("The battery life is 30%")
class Tablet:
    def battery_life(self):
        print("The battery lif is 40%")

L1 = Laptop()
L1.battery_life()

P1 = Phone()
P1.battery_life()

T1 = Tablet()
T1.battery_life()

"""
"""
#**Exercise 7 (Intermediate):** Create a parent class `Shape` with constructor and `area()` method.
# Child classes `Circle`, `Square`, `Rectangle` calculate different areas.
#Expected output: Area calculations for each shape.


class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        print(f"{self.name}, area: {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        print(f"{self.name}, area:{self.side * self.side}")

class Rectangle(Shape):
    def __init__(self,name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        print(f"{self.name}, area:{self.length * self.width}")

C1 = Circle("Circle",2)
C1.area()

S1 = Square("Square", 4)
S1.area()

R1 = Rectangle("Rectangle", 5, 5)
R1.area()

"""
"""
# **Exercise 8 (Intermediate):** Create a parent class `Bank` with constructor and `interest()` method.
# Child classes `SavingsAccount`, `CheckingAccount` override it with different interest rates.
# Expected output: Interest calculations for each account type.

class Bank:
    def __init__(self,interest):
        self.interest = interest
    def interest(self):
        pass

class SavingsAccount(Bank):
    def __init__(self,interest, savings):
        super().__init__(interest)
        self.savings = savings

    def interest(self):
        print(f"{self.savings}")

class CheckingAccount(Bank):
    def __init__(self, interest, CheckingAccount):
        super().__init__(interest)
        self.CheckingAccount = CheckingAccount

    def interest(self):
        print(f"{self.CheckingAccount}")

S1 = SavingsAccount( "5%", "Yes")
S1.interest()

C1 = CheckingAccount("5%", "Yes")
C1.interest()

"""

"""
#**Exercise 9 (Intermediate):** Create a parent class `Animal` with constructor taking name. Child classes `Lion`, `Elephant`, `Zebra` override `eat()` method.
#xpected output: Lion eats meat, Elephant eats plants, Zebra eats grass.

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        pass

class Lion(Animal):
    def __init__(self,name,eats):
        super().__init__(name)
        self.eats = eats

    def eat(self):
        print(f"The {self.name} eats {self.eats}")

class Elephant(Animal):
    def __init__(self,name,eats):
        super().__init__(name)
        self.eats = eats

    def eat(self):
        print(f"The {self.name} eats {self.eats}")

class Zebra(Animal):
    def __init__(self,name,eats):
        super().__init__(name)
        self.eats = eats

    def eat(self):
        print(f"The {self.name} eats {self.eats}")

L1 = Lion("Lion", "Meat")
L1.eat()

E1 = Elephant("Elephant","Plant")
E1.eat()

Z1 = Zebra("Zebra", "Grass")
Z1.eat()

"""
"""
# Exercise 10 (Intermediate): Create a parent class PaymentMethod with a constructor that takes amount.
# Child classes CreditCard, UPI, and NetBanking inherit from it and override a process() method with their own processing messages.
# Create one object for each child class with different amounts, then call process() on each.
# Expected Output:
# CreditCard processed payment of 5000 rupees
# UPI processed payment of 3000 rupees
# NetBanking processed payment of 7000 rupees

class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount

class CreditCard(PaymentMethod):
    def process(self):
        print(f"CreditCard processed payment of {self.amount} rupees")

class UPI(PaymentMethod):
    def process(self):
        print(f"UPI processed payment of {self.amount} rupees")

class NetBanking(PaymentMethod):
    def process(self):
        print(f"NetBanking processed payment of {self.amount} rupees")

c1 = CreditCard(5000)
c1.process()

u1 = UPI(3000)
u1.process()

n1 = NetBanking(7000)
n1.process()

"""




