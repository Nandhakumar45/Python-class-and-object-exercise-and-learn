a = 25
b = 4

print(a + b)  #29
print(a - b)  #21
print(a * b)  #100
print(a / b)  #6.2
print(a // b) #6
print(a % b)  #1
print(a ** b) #390,625

#2
a = 10
b = 5
c = 2

result = a + b * c ** 2 - a / b

print(result)  #28.0

#3

a = int(input("enter the number:"))
b = int(input("enter the number"))

result = (a+b) * (a+b) - (a-b) (a-b) / a * b
print(result(type(result)))


#4
total_seconds = 98765

hours = total_seconds // 3600

minutes = (total_seconds % 3600) // 60

seconds = total_seconds % 60

print(f"Hours = {hours} minutes =  {minutes} seconds = {seconds}")


#5
a = 100
b = 200
c = 100

print(a = b)
print(a != c)
print(b > a)
print(a <= c)
print(b >= c)

#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Smallest number
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# All three equal
all_equal = (a == b == c)

# Any two equal
any_two_equal = (a == b or b == c or a == c)

print("Largest:", largest)
print("Smallest:", smallest)
print("All three equal:", all_equal)
print("Any two equal:", any_two_equal)


#7
experience = int(input("enter the experience"))
age = int(input("enter the age"))

if (age >= 18 or age >=60) and experience >= 2:
    print("Hello")
else:
    print("age should not be less than 18 and greater than 60")

#8
password = "Python@123"
confirm_password = "Python@123"

# 1. Check whether both passwords match
print("Passwords match:", password == confirm_password)

# 2. Check whether password is different from Python123
print("Password is different:", confirm_password and password != "Python123")

# 3. Check whether password length is at least 8 characters
print("Password length is valid:", len(password) >= 8)

#9
a = True
b = False
c = True

print(a and b) #false
print(a or b) #True
print(not a)  #false
print(a and b or c) # True
print(a or b and c) # True
print(not (a and c)) #false

#10
experience = 6
rating = 4.5
disciplinary_action = False

eligible = ( experience >= 5 and rating >= 4 and disciplinary_action == False)
print("Eligible for promotion:", eligible)

#11
username = "admin"
password = "Admin@123"
is_account_active = True

login = (username == "admin" and password == "Admin@123" and is_account_active == True)
print(login)

#12
age = 25
membership_active = False
day_pass = True
is_banned = False

can_enter = age >= 18 and (membership_active or day_pass) and not is_banned

print("Can enter gym:", can_enter)


#13

a = 20

a += 10 #30
a -= 5  #15
a *= 2  #40
a /= 5  #4
a **= 2 #400

print(a)