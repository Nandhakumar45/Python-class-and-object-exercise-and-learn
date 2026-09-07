#1
try:
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter a number: "))
    number = number_1 / number_2

except ZeroDivisionError:
    print("Zero division error")

except ValueError:
    print("Enter number only")

else:
    print("You entered:", int(number))

#2
try:
    age = int(input("Enter a age: "))

except ValueError:
    print("Please enter a valid age")

else:
    print("Yours age is", age)

#3
numbers = [10, 20, 30, 40, 50]
try:
    index = int(input(f"Please enter a index:"))
    value = numbers[index]
    print(value)

except ValueError:
    print("Invalid Input")

except IndexError:
    print("Invalid Index")

else:
    print("Successfully retrieved the value")

#4
