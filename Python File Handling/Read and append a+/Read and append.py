#1
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\read and append\exercise1.txt", "a+") as file:
    file.write("Apple")

#2
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\read and append\exercise2.txt", "a+") as file:
    file.write("Mango\n")
    file.write("Banana\n")
    file.write("Orange")

#3
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\read and append\exercise3.txt", "a+") as file:
    file.write("Grapes")
    file.seek(0)
    data = file.read()
    print(data)

#4
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\read and append\exercise4.txt", "a+") as file:
    data = file.read()
    print(data)
    file.write("watermelon")
    file.seek(0)
    data = file.read()
    print(data)

#5
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\read and append\exercise5.txt", "a+") as file:
    fruit = input("Enter a fruit:")
    file.write(fruit)
    file.seek(0)
    data = file.read()
    print(data)

#6
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\read and append\exercise6.txt", "a+") as file:
    fruit = input("Enter fruit to search:")
    file.seek(0)
    data = file.read()
    if fruit in data:
        print("Fruit found")
    else:
        print("Fruit not found")




