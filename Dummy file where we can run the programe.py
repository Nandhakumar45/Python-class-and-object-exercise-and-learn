while True:
    name = input("Enter numbers:")
    with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\append mode.txt", "a") as file:
        file.write(f"{name}\n")

    if name == "exit":
        print("I exit from the condition")
        break