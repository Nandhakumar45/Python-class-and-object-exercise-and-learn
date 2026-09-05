#1
try:
    a = int (input("Enter the number:"))
    b = int (input("Enter the number:"))
    c = a/b
except ZeroDivisionError:
    print("Cannot divide by zero")

#2
try:
    age = int (input("Enter your age"))

except ValueError:
    print("Plesae enter a valid number")

#3
numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index (0 to 4): "))
    print(f"Value at index {index}: {numbers[index]}")
except IndexError:
    print("Invalid index")

#4
try:
    first_number = int(input("Enter the first number"))
    second_number = int(input("Enter the second number"))
    result = first_number / second_number
    print(result)

except ZeroDivisionError:
    print("Invalid number")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Invalid number")

#5
student = {
    "name": "John",
    "age": 25,
    "city": "Chennai"
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key not found in dictionary")

#6
try:
    number = int (input("Enter a number"))
    num    = 100 / number
except (ValueError, ZeroDivisionError):
    print("Enter the correct value")

#7
balance = 10000

try:
    withdraw = int(input("How much Rupees do you want to withdraw? "))

    if withdraw <= 0:
        print("Please enter a valid amount")

    elif withdraw > balance:
        print("Insufficient balance")

    else:
        print("Withdrawal successful")

except ValueError:
    print("Please enter a valid number")

#8
#My answer would be ZeroDivisionError
try:
    x = int("10")
    y = 0
    result = x / y
    print(result)

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Zero Division Error")

print("Finished")

#9
try:
    number = int(input("Enter number: "))
    print(100 / number)

except ValueError:
    #Type of error not defined
    print("Error")

except ZeroDivisionError:
    print("Cannot divide by zero")





