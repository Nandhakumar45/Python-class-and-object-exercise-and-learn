#1
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
    file.write("I am learning Python.")

#2
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
    file.write("Nandha\n")
    file.write("Ravi")

#3
name = input("Enter your name")
with open (r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
    file.write(name)
# #This is the best way to write a code when compared to previous one. add + \n in last line
# name = input("Enter your name: ")
#
# with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
#     file.write(name + "\n")
#4
for x in range(1,6):
    name = input("Enter your name:")
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
        file.write(f"{name}\n")
#5
for x in range(1,6):
    numbers = input("Enter numbers:")
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
        file.write(f"{numbers}\n")

# #This is the best way to write a code when compared to previous one. add + \n in last line
# name = input("Enter your name: ")
#
# with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
#     file.write(name + "\n")

#6
while True:
    name = input("Enter numbers:")
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
        file.write(f"{name}\n")

    if name == "exit":
        print("I exit from the condition")
        break
