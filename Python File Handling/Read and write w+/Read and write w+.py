#1
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise1.txt", "w+") as file:
    file.write("Nandha")
    file.seek(0)
    data = file.read()
    print(data)

#2
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise2.txt", "w+") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Orange")
    file.seek(0)
    data = file.read()
    print(data)

#3
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise3.txt", "w+") as file:
    file.write("1\n")
    file.write("2\n")
    file.write("3\n")
    file.write("4\n")
    file.write("5")
    file.seek(0)
    data = file.read()
    print(data)

#4
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise4.txt", "w+") as file:
    file.write("Python is easy to learn")
    file.seek(0)
    data = file.read()
    print(len(data))
#5
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise5.txt", "w+") as file:
    file.write("I am learning Python file handling")
    file.seek(0)
    data = file.read()
    words = data.split()
    print(len(words))
#6
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise6.txt", "w+") as file:
    file.write("python programming")
    file.seek(0)
    data = file.read()
    print(data.upper())

#7
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise7.txt", "w+") as file:
    file.write("Nandha\n")
    file.write("Arun\n")
    file.write("Kumar\n")
    file.write("Hello\n")
    file.write("Python")
    file.seek(0)
    data = file.read()
    print(len(data))

#8
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise8.txt", "w+") as file:
    file.write("85\n")
    file.write("90\n")
    file.write("78\n")
    file.write("88")
    file.seek(0)
    data = file.readlines()
    total = 0
    for mark in data:
        total += int(mark)
    print("Total Marks =", total)

#9
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise9.txt", "w+") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Orange\n")
    file.write("Mango")
    file.seek(0)
    data = file.read()
    if data == "Mango":
        print("Mango found")
    else:
        print("Mango Not Found")

#10
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise10.txt", "w+") as file:
    Report = {
        "Name" : "Nandha",
        "Age"  : "27",
        "City" : "Bangalore"
    }
    file.write(str(Report))
    file.seek(0)
    data = file.read()
    print(data)
