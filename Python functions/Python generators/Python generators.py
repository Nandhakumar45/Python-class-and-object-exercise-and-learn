# 0
def numbers():
    yield 10
    yield 20
    yield 30


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))


# 1
def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"


for i in fruits():
    print(i)

#2
def count():
    for i in range(1, 5):
        print(i)

#3
def count():
    for i in range(1, 6):
        yield i

for numbers in count():
    print(numbers)

#4
# answer step 1, 100 step 2, 200
def demo():
    print("Step 1")
    yield 100
    print("Step 2")
    yield 200
    print("Step 3")
    yield 300

gen = demo()
print(next(gen))
print(next(gen))


#5
def test():
    yield "Hello"

gen = test()
print(next(gen))

try:
    print(next(gen))
except StopIteration:
    print("Generator is finished")

#6

def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i

for number in even_numbers():
    print(number)


#7
def square(n):
    for i in range(1, n + 1):
        yield i * i

for value in square(4):
    print(value)


#8
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci(6):
    print(number)


#9

def positive_numbers(values):
    for number in values:
        if number > 0:
            yield number

values = [-3, 5, 0, -1, 8, 2]

for number in positive_numbers(values):
    print(number)


#10

def infinite_counter():
    number = 1

    while True:
        yield number
        number += 1

gen = infinite_counter()

for i in range(5):
    print(next(gen))




