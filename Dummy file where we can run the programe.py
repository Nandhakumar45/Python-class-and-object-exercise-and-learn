with open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\w+\exercise9.txt", "w+") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Orange\n")
    file.write("Mango")
    file.seek(0)
    data = file.read()
    if "Mango" in data:
        print("Mango found")
    else:
        print("Mango Not Found")