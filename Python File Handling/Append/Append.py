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

#4
for x in range(1,6):
    name = input("Enter your name:")
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
        file.write(f"{name}\n")



