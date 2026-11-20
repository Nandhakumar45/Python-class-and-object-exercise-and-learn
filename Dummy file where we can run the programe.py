username = input("Enter username: ").strip().lower()
password = input("Enter password: ").strip()

username_valid = len(username) >= 5

password_valid = (
    ("@" in password or "#" in password)
    and password[0].isupper()
)

if username_valid and password_valid:
    final_status = "ACCEPTED"
else:
    final_status = "REJECTED"

print("===== LOGIN VALIDATION =====")
print(f"Username       : {username}")
print(f"Username Valid : {username_valid}")
print(f"Password Valid : {password_valid}")
print(f"Final Status   : {final_status}")