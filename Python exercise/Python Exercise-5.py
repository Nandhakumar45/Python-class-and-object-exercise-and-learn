#1
for i in range(1, 21):
    print(i)

#2
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#3
number = int(input("Enter the number:"))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#4
number = int(input("Enter the number:"))

total = 0
for i in range(1, number+1):
    total += i

print(total)

#5
number = int(input("Enter the number:"))
odd = 0
even = 0
for i in range(1, number+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"even number {even} odd number {odd}")

#6
number = int(input("Enter a positive integer: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial =", factorial)

#7
number = input("Enter a number: ")

total = 0

for digit in number:
    total = total + int(digit)

print("Sum of digits =", total)

#8
word = input("Enter a word: ")

vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels =", count)