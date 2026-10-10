#1
name = "Nandha"
def show_name():
    print(name)
show_name()

#2
age = 27

def show_age():
    print(age)

def check_age():
    print(age)

show_age()
check_age()

#3
price = 100

def calculate():
    print(price + 20)
calculate()

#4
count = 10

def increase():
    global count
    count += 1

increase()
print(count)

#5
count = 0

def increase():
    global count
    count += 1

increase()
increase()
increase()

print(count)

#6
x = 100

def test():
    x = 50
    print(x)

test()

print(x)

#7
x = 100

def test():
    global x
    x = 50
    print(x)

test()
print(x)

#8
company = "Capgemini"

class Employee:

    def show_company(self):
        print(company)

emp = Employee()
emp.show_company()

#9
count = 0

def login():
    global count
    count += 1

login()
login()
login()
login()
print(count)

#10
balance = 1000


def deposit():
    global balance
    balance = balance + 500


def withdraw():
    global balance
    balance = balance - 200


def show_balance():
    print(balance)

deposit()
withdraw()
show_balance()


