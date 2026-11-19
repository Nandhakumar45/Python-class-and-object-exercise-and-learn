class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

Book_details = Book("A road", "Nandhakumar", 2020)

print(Book_details.title, Book_details.author, Book_details.year_published)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

Details = Car(make="BMW", model="2017", year=2020)
print(Details.make, Details.model, Details.year)


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def give_bonus(self):
        bonus_salary = self.pay + (self.pay * 0.10)
        return bonus_salary


Employee_details = Employee("Kumar", "Kumar", 20000)

print("First Name:", Employee_details.first)
print("Last Name:", Employee_details.last)
print("Current Salary:", Employee_details.pay)

new_salary = Employee_details.give_bonus()
print("Salary after 10% bonus:", new_salary)


