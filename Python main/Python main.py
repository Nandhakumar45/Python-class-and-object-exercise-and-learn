#1
def student_details():
    print("Student Name: Arun")
    print("Age: 25")
    print("Age: 25")

if __name__ == "__main__":
    student_details()

#2
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def main():
    print(add(20, 5))
    print(subtract(20, 5))
    print(multiply(20, 5))
    print(divide(20, 5))

if __name__ == "__main__":
    main()

#3
def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"

def main():
    print(check_number(8))

if __name__ == "__main__":
    main()

#4
def login():
    print("User logged in")
def open_dashboard():
    print("Dashboard opened")
def logout():
    print("User logged out")
def main():
    login()
    open_dashboard()
    logout()

if __name__ == "__main__":
    main()


#5
def calculate_average(x, y, z):
    sum = x + y + z
    average = sum / 3
    return average

def get_grade(average):
    if average >= 90:
        print("A")
    elif average >= 75 and average < 90:
        print("B")
    elif average >= 50 and average < 75:
        print("C")
    else:
        print("Fail")


def main():
    average = print(calculate_average(89, 90, 85))
    print(average)
    get_grade(average)

if __name__ == "__main__":
    main()


#6
print("Program started")
def display_message():
    print("Inside function")


def main():
    display_message()

if __name__ == "__main__":
    main()
    print("Program ended")



#8

import random


def play_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 20: "))
        attempts += 1

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print(f"Correct! Attempts: {attempts}")
            break


def main():
    print("Welcome to the Number Guessing Game!")
    play_game()


if __name__ == "__main__":
    main()

#9

employees = {}


def add_employee():
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))

    employees[name] = salary

    print("Employee added successfully!")


def display_employees():
    if not employees:
        print("No employees found.")
    else:
        print("\nEmployee Details:")

        for name, salary in employees.items():
            print(f"Name: {name}, Salary: {salary}")


def main():
    while True:
        print("\n1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            display_employees()

        elif choice == "3":
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
