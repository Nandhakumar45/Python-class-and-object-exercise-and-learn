'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info_person(self):
        print(f"{self.name}, {self.age}")

class Student(Person):
    def __init__(self, name, age, student_ID, grade):
        super().__init__(name,age)
        self.student_ID = student_ID
        self.grade = grade
    def display_info_student(self):
        self.display_info_person()
        print(f"{self.student_ID}, {self.grade}")

person_1 = Person("Nandha", "23")
student_1 = Student("Vishva", "23", "1", 23 )
student_1.display_info_student()
student_1.display_info_person()

'''

'''
********************** The second programme **********************************************


class Shape:
    def __init__(self,color):
        self.color = color

class Circle(Shape):
    def __init__(self,color, radius):
        super().__init__(color)
        self.radius = radius

class Rectangle(Shape):
    def __init__(self,color, width,height):
        super().__init__(color)
        self.width = width
        self.height = height

Shape_1 = Shape("Black")
circle_1 = Circle("Red", 2.3)
rectangle_1 = Rectangle("Orange", 22, 23)

print(circle_1.color, circle_1.radius)
print(Shape_1.color)
print(rectangle_1.color,rectangle_1.width, rectangle_1.height )

'''

'''
    *************************************Third Programme***************************************************
    
    class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"Color: {self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def display_circle(self):
        print(f"Radius: {self.radius}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_rectangle(self):
        print(f"Width: {self.width}, Height: {self.height}")

# Create objects
circle_1 = Circle("Red", 2.3)
rectangle_1 = Rectangle("Orange", 22, 23)

# Call methods to display info
circle_1.display_color()
circle_1.display_circle()

rectangle_1.display_color()
rectangle_1.display_rectangle()
    

'''

'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"Name: {self.name}")
        print(f"Sound: {self.sound}")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def display_dog(self):
        print(f"Dog Name: {self.name}")

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def display_cat(self):
        print(f"Cat Name: {self.name}")

Dog_1 = Dog("Nandha", "Bark")
Cat_1 = Cat("Vishva", "Meow")

Dog_1.display_dog()
Dog_1.make_sound()

Cat_1.display_cat()
Cat_1.make_sound()

'''
# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#
#     def show_info(self):
#         print(f"Brand: {self.brand} | Speed: {self.speed}", end=" | ")
#
#
# class Car(Vehicle):
#     def __init__(self, brand, speed, doors):
#         self.doors = doors
#
#     def show_info(self):
#         super().show_info()
#         print(f"Doors: {self.doors}")
#
#
# # Create object
# car_1 = Car("Toyota", 120, 4)
# car_1.show_info()

'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def call(self):
        print(f"{self.name}")
        print(f"{self.salary}")
        print(f"{self.department}")


c1 = Manager("Alice", 70000, "HR")
c1.call()
'''

'''
class Animal:
    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Call parent class method
        print("Dog barks")


# Create object
d1 = Dog()
d1.make_sound()

'''
'''
class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def product_method(self):
        print(f"name: {self.name} | price: {self.price}")
        print("hello world")

class Laptop(Product):
    def __init__(self, name, price, ram):
        super().__init__(name, price)
        self.ram = ram

    def product_method(self):
        print(f"name: {self.name} | price: {self.price} | ram {self.ram}")

L1 = Laptop("Dell", 65000, "16GB")
L2 = Product("Dell", 65000, )

L1.product_method()
L2.product_method()

'''
'''
 # Exercise 5 — Multi-Level Inheritance

class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name,employee_id)
        self.programming_language = programming_language

    def dev(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Language: {self.programming_language}")

D1 = Developer ("David", "E101", "Python")
D1.dev()

'''
'''
This code is wrong one:

class Rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def area(self, length, width):
        return length * width

class Box(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def area(self, length, width, height):
        return length * width * height

B1 = Box(10,10, 10)
B1.area()


This code is correctd one


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Box(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        base_area = super().area()
        return base_area * self.height


B1 = Box(10, 5, 5)

print(f"Area: {B1.area()}")
print(f"Volume: {B1.volume()}")

'''
'''
class Account:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance =  balance

    #def account_info(self):



class Savingsaccount(Account):
    def __init__(self,account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def display(self):
        print(f"Holder: {self.account_holder}")
        print(f"balance: {self.balance}")
        print(f"interest_rate: {self.interest_rate}")

S1 = Savingsaccount("Kumar", 5000, "7%")
S1.display()

'''
class Greeting:
    def greet(self):
        print("Hello")

class Welcome(Greeting):
    def greet(self):
        super().greet()
        print("Welcome to python")

W1 = Welcome()
W1.greet()
































