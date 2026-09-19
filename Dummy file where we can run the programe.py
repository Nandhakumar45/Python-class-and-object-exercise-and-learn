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