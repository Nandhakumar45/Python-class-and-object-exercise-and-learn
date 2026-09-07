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