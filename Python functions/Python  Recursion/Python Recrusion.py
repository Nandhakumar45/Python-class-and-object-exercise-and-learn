#1
def numbers(n):
    if n == 0:
        return

    numbers(n - 1)

    print(n)

numbers(5)

#2
def numbers(n):
    if n == 0:
        return

    print(n)
    numbers(n - 1)

numbers(5)

#3
def numbers(n):
    if n == 0:
        return

    print("Hello")
    numbers(n - 1)

numbers(4)

#4
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)
print(sum_numbers(5))

#5
def sum_numbers(n):
    if n == 0:
        return 0
    return n * sum_numbers(n - 1)
print(sum_numbers(5))

#6
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#7
def numbers(n):
    if n == 0:
        return 0

    return n + numbers(n-1)

a = numbers(4)
print(a)

#8
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(56789))

#9
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 4))

#10
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

#11
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))