c = True
correct_pin = "2068"
attempts = 0

while attempts < 3:
    pin = input("Enter the ATM pin:")

    if correct_pin == pin:
        print("PIN Verified Successfully")
        c = False
    else:
        print("Invalid Pin")

        attempts +=1
        remaining_attempts = 3 - attempts
        print(f"Remaining attempts: {remaining_attempts}")

    if attempts == 3:
        print("Account Locked")