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

























