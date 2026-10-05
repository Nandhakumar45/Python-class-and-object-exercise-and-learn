#1
def outer_function():
    count = 10
    def inner_function():
        nonlocal count
        count += 5

    inner_function()
    print(count)
outer_function()

#2
def outer_function():
    name = "Nandha"
    def inner_function():
        nonlocal name
        name = "leela"
    inner_function()
    print(name)
outer_function()

#3
def outer_function():
    balance = 1000
    def deposit():
        nonlocal balance
        balance += 500
    deposit()
    print(balance)
outer_function()

#4
def outer_function():
    balance = 2000
    def withdraw():
        nonlocal balance
        balance = balance - 300
    withdraw()
    print(balance)
outer_function()

#5

def outer_function():
    count = 0
    def increment():
        nonlocal count
        count +=1
    increment()
    increment()
    increment()
    print(count)
outer_function()
#6

def outer_function():
    message = "hello"
    def inner_function():
        nonlocal message
        message += "world"
    inner_function()
    print(message)
outer_function()

#7
def temperatues():
    temperature = 30
    def inner_function():
        nonlocal temperature
        temperature += 5
    inner_function()
    print(temperature)
temperatues()
#8
def outer_function():
    total = 100
    def add_item():
        nonlocal total
        total += 50
    add_item()
    print(total)
outer_function()

#9
def outer_function():
    score = 0
    def win():
        nonlocal score
        score += 10
    def bonus():
        nonlocal score
        score += 5

    win()
    bonus()
    win()
    print(score)
outer_function()

#10
def outer_function():
    salary = 30000
    def increment():
        nonlocal salary
        salary += 5000
    increment()
    print(salary)
outer_function()

#11
def outer_function():
    x = 10
    def inner_function1():
        nonlocal x
        x += 5
    def inner_function2():
        nonlocal x
        x = x * 2
    inner_function1()
    inner_function2()
    print(x)
outer_function()





