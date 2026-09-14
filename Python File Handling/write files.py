#1
'''
Exercise 1 — Write your name
Create name.txt and write:
'''
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
file.write("My name is Nandha")
file.close()

#2
'''
Exercise 2 — Write multiple lines
Create details.txt and write:
Name: Nandha
Age: 27
Language: Python
'''
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
file.write("Name: Nandha\n")
file.write("Age: 27\n")
file.write("Language: Python")
file.close()

#3
'''
Exercise 3 — Using \n
Create fruits.txt and write:
Apple
Banana
Orange
Mango
'''
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
file.write("Apple\n")
file.write("Banana\n")
file.write("Orange\n")
file.write("Mango\n")
file.close()

#4
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
file.write("10\n")
file.write("20\n")
file.write("30\n")
file.write("40\n")
file.write("50\n")
file.close()

#5
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
file.write("I am learning Python file handling.\n")
file.write("I will practice every day.\n")
file.close()

#6
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
fruits = ["Apple\n", "Banana\n", "Orange\n", "Mango\n"]
file.writelines(fruits)
file.close()

#7
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
names = ["Nandha\n", "Kumar\n", "Rahul\n", "Arun\n", "Vijay\n"]
file.writelines(names)
file.close()

#8
file = open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")
numbers = ["10", "20", "30", "40", "50"]
file.writelines(numbers)
file.close()

#9
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "w")

student = [
    "Name: Nandha\n",
    "Age: 27\n",
    "Course: Python\n",
    "Topic: File Handling\n"
]

file.writelines(student)
file.close()


file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Write.txt", "r")

content = file.read()
print(content)

file.close()


