# 1
def show_name():
    name = "Nandha"
    print(name)
show_name()


# 2
def calculate():
    a = 20
    b = 30
    c = a + b
    print(c)

calculate()
# 3
count = 10

def display():
    print(count)

display()

#4
balance = 1000

def deposit():
    global balance
    balance += 500

deposit()
print(balance)

#5
x = 100

def test():
    x = 200
    print(x)
test()
print(x)

#6
def outer_function():
    x = 50

    def inner_function():
        print(x)
    inner_function()

outer_function()

#7
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print(x)
    inner()
outer()

#8
def outer():
    count = 0

    def inner():
        nonlocal count
        count +=1
    inner()
    inner()
    inner()

print(count)

#9
x = 10
def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
        print(x)
    inner()
    outer()
print(x)

#10
balance = 1000

def bank_account():

    def deposit():
        global balance
        balance = balance + 500

    def withdraw():
        global balance
        balance = balance - 200

    deposit()
    withdraw()
print(balance)
bank_account()

