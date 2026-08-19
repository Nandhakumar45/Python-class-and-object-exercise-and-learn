#You have to learn what is the difference between module operator and % operator

# have to work on count

word = "banana"
count = 0

for character in word:
    count += 1

print(count)

word = "banana"
count = 0

for character in word:
    count += 1

print(count)

word = "programming"
vowels = "aeiou"
count = 0

for character in word:
    if character in vowels:
        count += 1

print(count)


#Find the largest numbers
numbers = [10, 25, 8, 99, 45]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)