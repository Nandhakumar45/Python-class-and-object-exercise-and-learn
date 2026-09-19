with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise6.txt", "r+") as file:

    # 1. Read the existing content
    data = file.read()
    print("Existing content:")
    print(data)

    # 2. Write new content
    file.write("\nThis is line number 2.")

    # 3. Move the pointer back to the beginning
    file.seek(0)

    # 4. Read the complete file again
    data = file.read()
    print("Content after writing:")
    print(data)

#1
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise1.txt", "r+") as file:
    data = file.read()
    print(data)

#2
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise2.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("\nLine 2")
#3
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise3.txt", "r+") as file:
    data = file.read()
    print(data)
    file.seek(0)
    data = file.read()
    print(data)
#4
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise4.txt", "r+") as file:
    file.write("\nHello")
    file.seek(0)
    data = file.read()
    print(data)
#5
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise5.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("\nThis is line 2")
    file.seek(0)
    data = file.read()
    print(data)

#6
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise6.txt", "r+") as file:
    file.seek(5)
    file.write("XYZ")
    #In this position xyz appears "ABCDXYZHIJ"
#7
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise7.txt", "r+") as file:
    data = file.read(6)
    print(data) #It prints only "python"
    file.seek(0)
    data = file.read()
    print(data) #It prints all the string present in the document

#8
with open(
    r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise8.txt", "r+") as file:
    file.seek(6)
    file.write("Python")

    file.seek(0)  # Move the pointer to the beginning
    data = file.read()
    print("Final content:", data)

#9
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\employee.txt", "r+") as file:
    data = file.read()
    print(data)
    file.write("\nExperience: 7 years")
    file.seek(0)
    data = file.read()
    print(data)
#10
#Not sure how to solve this
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\r+\exercise10.txt", "r+") as file:
    print("Position:", file.tell())
    data = file.read(4)
    print("Read:", data)
    print("Position:", file.tell())
    file.write("ABC")
    file.seek(0)
    data = file.read()
    print("Final content:", data)