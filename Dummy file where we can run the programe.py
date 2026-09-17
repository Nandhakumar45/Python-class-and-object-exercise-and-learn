for x in range(1,6):
    name = input("Enter your name:")
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
        file.write(f"{name}\n")