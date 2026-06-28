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