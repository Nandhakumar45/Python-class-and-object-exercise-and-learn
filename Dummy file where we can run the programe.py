#1
#this is the first programme
print("Hello world")

#2
#this two variable stores the values
name = "nandha"
age = 27

#3

a = 10
b = 20

# Addition
# Subtraction
# Multiplication
# Division

#4

length = 20 # a length variable stores the value in int formate
width = 20 # a width variable stores the width value in int formate

area = length * width # a area variable calculate the length and width

print(area) #it prints the output

#5
print("Python")
#print("Java")
#print("Selenium")
print("Playwright")

#6
#They are two types of loops
#For and while loop
#For loops works it is upon the the given start and end condition but while loop works when the condition terminiates


#7
# outer loop
i = 1

while i <=5:
    #inner loop
    #counter initialization
    j = 1
    while j<=5:

        print(j, end = "")
        # counter increment
        j += 1
    i +=1
    print()

#8
'''
Python Learning
Topic: Comments
Level: Beginner
'''

#9
"""
Python Learning
Topic: Comments
Level: Beginner
"""

#10
#print("Java")

#multiline comments
# Python Learning
# Topic: Comments
# Level: Beginner

''' a = 20'''

#11

def addition(a, b):
    '''
    :param a:
    :param b:
    :return:
    '''
    return a + b
print(addition(15, 15))

#12
def multiplication(a, b):
    '''
    :param a:
    :param b:
    :return:
    '''
    return a * b
print(multiplication(15, 15))
print(multiplication.__doc__)

#13
def calculate_area(length, width):
    """
    :param length:
    :param width:
    :return:
    """
    area = length * width
    return area
print(calculate_area(5, 5))


