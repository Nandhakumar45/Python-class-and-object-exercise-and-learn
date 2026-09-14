#1
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Hello.txt", "r")
content = file.read()
print(content)
file.close()

#2
#This program state that how to print the first line in the programme
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Hello2.txt", "r")
content = file.readline()
print(content)
file.close()
#To print the second line follow this step uisng the index of the programming
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Hello2.txt", "r")

lines = file.readlines()

print(lines[1])

file.close()


#3
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Hello2.txt", "r")
content = file.readlines()
print(content)
file.close()


#4
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Hello2.txt", "r")
content = file.read()
print(len(content))
file.close()

#5
file = open(r"C:\Users\320287287\OneDrive - Philips\Desktop\File Handling\Read\Hello3.txt", "r")
content = file.read()

if "Python" in content:
    print("Word exists in the file")
else:
    print("Word not found")

file.close()


