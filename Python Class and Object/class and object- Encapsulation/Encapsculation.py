"""
************************Exercise 1*****************************
Create a class Student that:

Has a private variable __marks
Has a method get_marks() to view the marks
Has a method set_marks(value) that:

Only allows marks between 0 and 100
Prints "Invalid marks!" if outside that range

******************

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("The value is out of range")

S1 = Student(88)
print(S1.get_marks())
print(S1.set_marks(56))

"""

"""
************************Exercise 2*****************************

Exercise 2: Bank Account

Create a class BankAccount.

Requirements
Private attribute: __balance
Constructor accepts balance.
Create:
get_balance()
deposit(amount)
withdraw(amount)
Rules
Deposit amount must be greater than 0.
Withdrawal amount cannot exceed balance.

"""
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be greater than 0")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")


A1 = BankAccount(1000)

print("Initial Balance:", A1.get_balance())

A1.deposit(500)

A1.withdraw(200)

print("Final Balance:", A1.get_balance())


****************Exercise 2*****************
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        if value >= 0:
            self.__salary = value
            #return value
            return self.__salary
        else:
            print("Value is should not less than 0 )")

E1 = Employee(99)
print(E1.get_salary())
print(E1.set_salary(44))

"""
"""
#****************************Exercise 3*******************

class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value >= 0:
            self.__price = value
            return self.__price
        else:
            print("The value should be greater that 0")

P1 = Product(34)
P1.set_price(56)
print(P1.get_price())
print(P1.set_price(44))

"""
"""
**Problem 1 (Easy) — Basic Private Attribute**
Create a class `BankAccount` with a private attribute `__balance`. Initialize it in the constructor with a starting balance.
Add a getter method `get_balance()` that returns the balance.

Expected output:
```
account = BankAccount(1000)
print(account.get_balance())
# Output: 1000

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())

"""
""""
**Problem 2 (Easy) — Getter and Setter**
Create a class `Student` with a private attribute `__marks`. Add a getter `get_marks()` and a setter `set_marks(value)`
that only allows values between 0 and 100. If an invalid value is passed, print an error message and don't update.

Expected output:
```
s = Student()
s.set_marks(85)
print(s.get_marks())   # Output: 85
s.set_marks(150)        # Output: Invalid marks!
print(s.get_marks())   # Output: 85 (unchanged)

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks!")

S = Student(5)
S.set_marks(85)
print(s. get_marks())
S.set_marks(150)
print(S.get_marks())

"""
"""
**Problem 3 (Easy) — Using @property**
Create a class `Circle` with a private attribute `__radius`. Use the `@property` decorator to create a `radius`property with a getter and setter.
The setter should reject negative values.

Expected output:
```
c = Circle(5)
print(c.radius)   # Output: 5
c.radius = -2      # Output: Radius cannot be negative!
print(c.radius)   # Output: 5
```

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius cannot be negative!")
        else:
            self.__radius = value

c = Circle(5)
print(c.radius)   # Output: 5
c.radius = -2      # Output: Radius cannot be negative!
print(c.radius)   # Output: 5

"""
"""
**Problem 4 (Medium) — Deposit and Withdraw with Validation**
Extend the `BankAccount` class. Add `deposit(amount)` and `withdraw(amount)` methods.
Withdrawal should fail if the amount exceeds the balance, printing an error message instead.

Expected output:
```
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # Output: 1500
account.withdraw(2000)          # Output: Insufficient balance!
print(account.get_balance())   # Output: 1500
```

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # Output: 1500
account.withdraw(2000)          # Output: Insufficient balance!
print(account.get_balance())   # Output: 1500

"""
"""
# **Problem 5 (Medium) — Read-Only Property**
# Create a class `Employee` with private attributes `__name` and `__id`. Make `id` a
# read-only property (getter only, no setter)
# since an employee's ID should never change after creation.
#
# Expected output:
# ```
# e = Employee("Kumar", 101)
# print(e.id)     # Output: 101
# e.id = 102       # Should raise AttributeError (can't set attribute)


class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id     = id

    @property
    def id(self):
        return self.__id

e = Employee("Kumar", 101)
print(e.id)     # Output: 101
e.id = 102       # Should raise AttributeError (can't set attribute)

"""
"""
# **Problem 6 (Medium) — Encapsulation with Calculated Property**
# Create a class `Rectangle` with private attributes `__length` and `__width`. Add a property `area`
# that calculates and returns length × width (no setter needed since it's derived).
#
# Expected output:
# ```
# r = Rectangle(5, 4)
# print(r.area)   # Output: 20


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def area(self):
        return self.__length * self.__width


r = Rectangle(5, 4)
print(r.area())   # Output: 20

"""
"""
**Problem 7 (Medium) — Name Mangling Check**
Create a class `Wallet` with a double-underscore private attribute `__money`. Try accessing `wallet._Wallet__money`
directly from outside the class (name mangling) and also try `wallet.__money` to see the difference.

Expected output:
```
w = Wallet(500)
print(w._Wallet__money)   # Output: 500
print(w.__money)           # Output: AttributeError

class Wallet:
    def __init__(self, money):
        self.__money = money

    def wallet_balance(self):
        return self.__money


w = Wallet(500)
print(w._Wallet__money)   # 500 — name mangling lets you access it this way

try:
    print(w.__money)
except AttributeError as e:
    print("AttributeError:", e)

"""
"""
**Problem 8 (Hard) — Multiple Private Attributes with Validation**
Create a class `Person` with private attributes `__name`, `__age`, and `__email`. Add getters/setters for all three.
The age setter should reject negative values; the email setter should reject any string without "@" in it.

Expected output:
```
p = Person("Arun", 25, "arun@gmail.com")
p.set_age(-5)             # Output: Invalid age!
p.set_email("arungmail")  # Output: Invalid email!
print(p.get_age())        # Output: 25
print(p.get_email())      # Output: arun@gmail.com

class Person:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_age(self, value):
        if value < 0:
            print("Invalid age!")
        else:
            self.__age = value

    def set_email(self, value):
        if "@" not in value:
            print ("Invalid email!")
        else:
            self.__email = value

p = Person("Arun", 25, "arun@gmail.com")
p.set_age(-5)             # Output: Invalid age!
p.set_email("arungmail")  # Output: Invalid email!
print(p.get_age())        # Output: 25
print(p.get_email())      # Output: arun@gmail.com

"""
"""
**Problem 9 (Hard) — Encapsulation in Inheritance**
Create a base class `Vehicle` with a private attribute `__speed`. Create a getter/setter for it.
Create a subclass `Car` that tries to access `__speed` directly (it should fail) but works fine using the inherited getter/setter methods.

Expected output:
```
car = Car("Toyota")
car.set_speed(120)
print(car.get_speed())   # Output: 120
# Direct access car.__speed from Car class would fail (name mangling)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        self.__speed = value


class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def try_direct_access(self):
        # This will fail because __speed mangles to _Car__speed here,
        # not _Vehicle__speed (where it was actually created)
        try:
            return self.__speed
        except AttributeError as e:
            return f"AttributeError: {e}"


car = Car("Toyota")
car.set_speed(120)
print(car.get_speed())   # Output: 120

print(car.try_direct_access())  # Output: AttributeError: 'Car' object has no attribute '_Car__speed'

"""

















