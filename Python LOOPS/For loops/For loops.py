#1
for i in range(1, 21):
    print(i)
#2
for i in range(20, 1):
    print(i)
#3
for i in range(1, 50):
    z = i / 2
    print(z)
#4
for i in range(1, 50):
    z = i / 2 != 0
    print(z)
#5
#Not sure how do this

#6
fruits = ["apple", "banana", "cherry", "orange"]
for i in fruits:
    print(i)

#7
word = "PYTHON"
for i in word:
    print(i)

#8
word = "banana"
for i in len(word):
    print(i)

#9
word = "programming"
x = ["a", "e", "i", "o", "u"]
for x in word:
    print(len(x))

#10
#Not sure how to solve this

#11
#Not sure how to solve this

#12
for i in range(1, 100, 5):
    print(i)

#13
for i in range(1, 20):
    if i == 10:
        continue
    print(i)

#14
for i in range(1, 20):
    if i == 15:
        break
    print(i)

#15
vegetables = ["Pumpkin", "Carrot"]
fruits = ["Apple", "Orange", "Cherry"]

for x in vegetables:
    for y in fruits:
        print(x,y)

