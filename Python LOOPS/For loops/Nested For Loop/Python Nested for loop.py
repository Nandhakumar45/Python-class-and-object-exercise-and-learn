#1
for i in range(3):
    for j in range(2):
        print(i , j)

#2
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

"""- print("*") prints a star and moves to the next line.
- print("*", end="") prints a star but does not move to the next line.
The end="" replaces the default newline (\n) with an empty string.

Therefore, the inner loop prints all 5 stars on the same line. 
The separate print() moves the cursor to the next line after those 5 stars are printed."""


#3
for i in range(3):
    for j in range(i):
        print("python")

#4
for i in range(4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

#5
for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()


#6
for i in range(6):
    for j in range(1, i + 2):
        print(j,  end=" ")
    print()

"""Think of it as: Start printing at 1, and keep printing until you reach the stop value.
1. Understand range(1, i + 2)
range(start, stop) means:
- 1 → starting value of j.
- i + 2 → stopping value, calculated using the current value of i.
- Python does not include the stopping value.
2. See what happens for each value of i
The outer loop is for i in range(6), so i takes the values 0, 1, 2, 3, 4, 5.
When i = 0
range(1, 0 + 2) → range(1, 2)
Values of j: 1

When i = 1
range(1, 1 + 2) → range(1, 3)
Values of j: 1, 2

When i = 2
range(1, 2 + 2) → range(1, 4)
Values of j: 1, 2, 3

Notice the pattern: every time i increases by 1, the inner loop prints one additional number."""

#7
for i in range(1, 6):

    for j in range(1, 6):
        print( i * j, end = " ")
    print()

#8
list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]

for i in list1:
    for j in list2:
        if i == j:
            print(i)

#9
browsers = ["Chrome", "Firefox"]
tests = ["Login", "Search", "Logout"]

for i in browsers:
    for j in tests:
        print(i , j)

#10

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 5:
            print(numbers[i], numbers[j])







