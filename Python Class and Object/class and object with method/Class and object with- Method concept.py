
# First, create a class called Car with attributes like brand, model, and year. Add a method that displays the car details.
# Second, create a class called BankAccount with attributes like account_number and balance, and add methods to deposit, withdraw, and check the balance.
# And third, create a class for a Book with attributes like title, author, and pages, and add a method to display a summary of the book.
# Once you try them out, we can refine or expand!

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_details(self):
        print("The Brand:", self.brand)
        print("The Model Number:", self.model)
        print("The Year:", self.year)


# Create a car object
car1 = Car("Apple", "Mercedes", "2008")
car1.car_details()


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


# Create a bank account object
account1 = BankAccount(account_number="123", balance=100)
account1.show_balance()
account1.deposit(50)
account1.withdraw(30)
account1.show_balance()


class Book:
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def display(self):
        print("The title:", self.title)
        print("Pages:", self.page)


# Create a book object
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book1.display()