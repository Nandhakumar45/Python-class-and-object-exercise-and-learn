"""
1. **Easy Problem**:
   Problem: Create an abstract class `Shape` with an abstract method `area()`.
   Then create a `Square` subclass that calculates the area given its side length.
   Expected Output:
   When you create a `Square` with a side of 4, and call `area()`, it should print "Area: 16."

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return f"Area: {self.length * self.length}"

square = Square(4)
print(square.area())

"""
"""
# **1. (Easy)** Create abstract class `Animal` with abstract method `sound()`. Create subclasses `Dog` and `Cat` that implement it differently.
# ```
# Expected:
# Dog().sound() -> "Woof!"
# Cat().sound() -> "Meow!"

from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

dog = Dog()
dog.sound()
cat = Cat()
cat.sound()

"""
"""
**2. (Easy)** Create abstract class `Shape` with abstract method `area()`. Create a `Circle` subclass (takes `radius`) that returns
area rounded to 2 decimals using `3.14 * r * r`.
```
Expected:
Circle(5).area() -> 78.5

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius * self.radius, 2)


C1 = Circle(5)
print(C1.area())  # -> 78.5

"""
"""
**3. (Easy-Medium)** Create abstract class `Employee` with abstract method `calculate_salary()`.
Create `FullTimeEmployee` (fixed monthly salary) and `Intern` (stipend per day × number of days) subclasses.
```
Expected:
FullTimeEmployee(50000).calculate_salary() -> 50000
Intern(500, 20).calculate_salary() -> 10000


from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, full):
        self.full = full

    def calculate_salary(self):
        return self.full


class Intern(Employee):
    def __init__(self,SPD, NOD):
        self.SPD = SPD
        self.NOD = NOD
    def calculate_salary(self):
        return self.SPD * self.NOD

f1 = FullTimeEmployee(50000)
print(f1.calculate_salary())
I1 = Intern(500, 20)
print(I1.calculate_salary())

"""
"""
# **4. (Medium)** Create abstract class `Vehicle` with **two** abstract methods: `start_engine()` and `fuel_type()`.
# Create `PetrolCar` and `ElectricCar` subclasses implementing both methods differently.
# Try instantiating `Vehicle()` directly and observe the error.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class PetrolCar(Vehicle):
    def start_engine(self):
        return "Starting petrol engine..."

    def fuel_type(self):
        return "Petrol"


class ElectricCar(Vehicle):
    def start_engine(self):
        return "Starting electric motor silently..."

    def fuel_type(self):
        return "Battery"


# Test
p1 = PetrolCar()
print(p1.start_engine())   # Starting petrol engine...
print(p1.fuel_type())      # Petrol

e1 = ElectricCar()
print(e1.start_engine())   # Starting electric motor silently...
print(e1.fuel_type())      # Battery

# Try instantiating Vehicle directly
v = Vehicle()   # ❌ raises TypeError

"""








