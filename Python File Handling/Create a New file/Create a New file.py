#1
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise1.txt", "x") as file:
    file.write("I am learning Python file handling.")

#2
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise2.txt", "x") as file:
    file.write("Nandhakumar")

#3
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise3.txt", "x") as file:
    file.write("Python\n")
    file.write("File Handling\n")
    file.write("X Mode\n")
#4
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise4.txt", "x") as file:
    file.write("Learning X mode")

#5
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise5.txt", "x") as file:
    numbers = ["10\n", "20\n", "30\n", "40\n", "50\n"]
    file.writelines(numbers)
#6
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise6.txt", "x") as file:
        file.write("I ran one time")
#7
try:
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\exercise7.txt", "x") as file:
        file.write("I ran one time")

except FileExistsError:
    print("File already exits")

#8
try:
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\student.txt", "x") as file:
        file.write("Student file created successfully.")

except FileExistsError:
    print("Student file already exists.")

#9
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\name.txt", "x") as file_1:
    file_1.write("Nandhakumar")
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\age.txt", "x") as file_2:
    file_2.write("28")
with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\city.txt", "x") as file_3:
    file_3.write("Chennai")

#10
try:
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\employee.txt", "x") as file:
        data = {
        "Name": "Nandhakumar",
        "Department": "Software Testing",
        "Experience": "7 years",
        "Skill": "Python"
        }
        file.write(str(data))
except FileExistsError:
    print("Data already exists")





