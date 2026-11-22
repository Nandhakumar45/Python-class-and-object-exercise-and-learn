''' 1
Correct ATM PIN: 2468
Give the user a maximum of 3 attempts.
Use a while loop.
Ask the user to enter the PIN.
If the PIN is correct → PIN Verified Successfully.
If the PIN is wrong → Invalid PIN.
Display remaining attempts after every unsuccessful attempt.
After 3 failed attempts → ATM Card Blocked.
If PIN is correct, stop the loop immediately.
'''
correct_pin = "2468"
attempts = 0

while attempts < 3:
    pin = input("Enter the ATM pin:")

    if correct_pin == pin:
        print("PIN Verified Successfully")
    else:
        print("Invalid Pin")

        attempts +=1
        remaining_attempts = 3 - attempts
        print(f"Remaining attempts: {remaining_attempts}")

    if attempts == 3:
        print("Account Locked")


''' 2
Correct username: employee01
Correct password: Work@2026
Maximum 4 login attempts.
Use a while loop.
If both username and password are correct → Employee Login Successful.
If username is incorrect → Incorrect Username.
If password is incorrect → Incorrect Password.
If both are incorrect → Invalid Username and Password.
Increase the attempt counter after every unsuccessful login.
Display remaining attempts after each failure.
After 4 failed attempts → Employee Account Locked.
If login succeeds, stop the loop.
'''
correct_username = "employee01"
correct_password = "Work@2026"

attempts = 0

while attempts < 4:
    user_name = input("Enter the username: ")
    password = input("Enter the password: ")

    if user_name == correct_username and password == correct_password:
        print("Employee Login Successful")
        break

    else:
        if user_name != correct_username and password != correct_password:
            print("Invalid Username and Password")
        elif user_name != correct_username:
            print("Incorrect Username")
        else:
            print("Incorrect Password")

        attempts += 1
        remaining_attempts = 4 - attempts
        print(f"Remaining attempts: {remaining_attempts}")

        if attempts == 4:
            print("Employee Account Locked")


''' 3
Correct OTP: 583921
Maximum 3 OTP attempts.
Use a while loop.
Ask the user to enter the OTP.
If OTP is correct → Payment Verified.
If OTP is incorrect → Incorrect OTP.
Display remaining attempts after every unsuccessful verification.
After 3 failed attempts → Payment Failed - Transaction Cancelled.
If OTP is verified, display Payment Processing.
Stop the loop immediately after correct OTP verification.
'''

correct_OTP = 583921

attempts = 0

while attempts < 3:
    OTP = input("Enter the OTP")

    if OTP == correct_OTP:
        print("correct OTP")
        print("OTP is in progress")
        break

    else:
        print("Incorrect OTP")
        attempts += 1
        remaining_attempts = 3 - attempts
        print(remaining_attempts)
        if attempts == 3:
            print("Payment Failed - Transaction Cancelled")

''' 4
Correct license key: LIC-2026-ABCD
Maximum 5 attempts.
Use a while loop.
Ask the user to enter the license key.
If the key is correct → License Activated Successfully.
If incorrect → Invalid License Key.
Display remaining attempts after each failure.
When remaining attempts reach 3 or fewer → display Warning: Multiple Invalid Attempts.
After 5 failed attempts → License Activation Blocked.
If activation succeeds, stop the loop.
'''

Correct_license_key: "LIC-2026-ABCD"

attempts = 0

while attempts < 5:
    license = input("Enter the license")

    if license == Correct_license_key:
        print("License Activated Successfully")
        break

    else:
        print("Invalid License Key")
        attempts += 1
        remaining_attempts = 5 - attempts
        print(remaining_attempts)
        if remaining_attempts < 3:
            print("Multiple Invalid attempts")
        if remaining_attempts == 5:
            print("license Activation Blocked")

''' 5
Maximum test execution attempts: 3.
Use a while loop.
Ask the tester to enter the test result:
- pass
- fail
If result is pass → Test Passed.
If result is fail → Test Failed.
If the test fails, increment the failure counter and allow retry.
Display remaining retries after each failure.
If it passes on the second or third attempt → Test Passed After Retry.
If all 3 attempts fail → Test Case Failed - Retry Limit Reached.
Reject invalid input (anything other than pass or fail) and ask again without consuming an execution attempt.
Stop the loop immediately when the test passes.
'''
attempts = 0

while attempts < 3:

    while True:
        result = input("Enter the test result (pass/fail): ").lower()

        if result == "pass" or result == "fail":
            break
        else:
            print("Invalid input. Enter pass or fail.")

    if result == "pass":
        if attempts == 0:
            print("Test Passed")
        else:
            print("Test Passed After Retry")
        break

    else:
        print("Test Failed")
        attempts += 1
        remaining_attempts = 3 - attempts
        print(f"Remaining retries: {remaining_attempts}")

        if attempts == 3:
            print("Test Case Failed - Retry Limit Reached")
