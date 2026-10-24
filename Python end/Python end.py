#1
print("Hello", end="")
print("World")
# HelloWorld is the output

#2
print("Good", end=" ")
print("Morning")

#Good Morning

#3
print("Python", end="\n")
print("Java")
#Python
#Java

#4
print("A", end="-")
print("B", end="-")
print("C")

#A-B-C

#5
print("One", end=" ")
print("Two", end=" ")
print("Three", end=" ")
print("Four")

#one Two Three Four

#6
for i in range(1, 6):
    print(i, end="")

#12345

#7
for i in range(1, 6):
    print(i, end=" ")
print("Done")

#1 2 3 4 5
#Done

#8
for i in range(4):
    print("*", end="")

#****

#9
print("Hello", end=" ")
print("World")
print("Python", end="")
print("Programming")

#Hello World
#PythonProgramming

#10
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# * * *
# * * *
# * * *


print("Hello", end="")
print("Finished")
print("Finished")


print("Hello", end="")
print("Finished")
