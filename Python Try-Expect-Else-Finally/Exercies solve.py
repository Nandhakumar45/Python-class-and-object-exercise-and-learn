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
