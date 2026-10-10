#1
two_numbers = lambda a, b: a+b
print(two_numbers(10, 20))

#2
square = lambda x : x * x
print(square(6))

#3
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))

#4
is_greater = lambda x, y: x if x > y else y
print(is_greater(15, 25))

#5
convert = lambda C:  (C * 9/5 + 32)
print(convert(30))

#6
multiply = lambda a,b,c : a * b * c
print(multiply(2,3,4))

#7
length = lambda a: len(a)
print(length("Python"))

#8
numbers = [23, 15, 42, 31, 18]

numbers.sort(key=lambda x: x % 10)

print(numbers)

#9
numbers = [5, 12, 8, 20, 3, 15]

output = list(filter(lambda x: x > 10, numbers))

print(output)

#10
discount_price = lambda price, discount: price - (price * discount / 100)

print(discount_price(1000, 20))