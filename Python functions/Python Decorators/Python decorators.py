#1
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello world")
greet()

#2
def pizza_decorator(func):
    def wrapper():
        print("Preparing the pizza base...")
        func()
        print("Pizza is served!")
    return wrapper

@pizza_decorator
def make_pizza():
    print("Pizza is ready!")

make_pizza()

#3
def twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@twice
def say_hello():
    print("Hello")

say_hello()

#4
def status_decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")
    return wrapper

@status_decorator
def  greet():
    print("hello python")

greet()

#5 not sure how to solve this
def my_decorator(func):
    def wrapper():
        return func()
    return wrapper

@my_decorator
def calculate():
    return 5 * 5

print(calculate())
"""Why? calculate() returns 25 to the wrapper. The wrapper must return that same value to print().

Remember the difference:
- func() calls the function.
- return func() calls the function and passes its result back to the caller."""
#6
def logger(func):
    def wrapper():
        print("Executing function")
        func()
    return wrapper

@logger
def login():
    print("User logged in")
login()

#7
def star_decorator(func):
    def wrapper():
        print("**********")
        func()
        print("**********")
    return wrapper

@star_decorator
def welcome():
    print("Welcome to Python")

welcome()

#8

"""xercise 8 — Support function arguments
Needs correction

There are two issues:
1. wrapper() doesn't accept a and b.
2. It doesn't call func() or return the result.
A general solution is to use *args and **kwargs.

Important concept:
- *args accepts positional arguments such as 10 and 20.
- **kwargs accepts keyword arguments such as a=10 and b=20.
- func(*args, **kwargs) passes those arguments to the original function.

"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calculating...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(10, 20))

#9
def repeat_three(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper

@repeat_three
def count():
    print("Python")
count()

#10
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(4)
def hello():
    print("Hello")

hello()
