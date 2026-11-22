#1
ATM = True

account_balance = int(input("Enter the account balance: "))

while ATM:
    withdrawal_amount = int(input("Enter the withdrawal amount: "))

    after_withdrawal = account_balance - withdrawal_amount

    if withdrawal_amount <= 0:
        print("Invalid Amount")

    elif withdrawal_amount > account_balance:
        print("Insufficient Balance")

    elif after_withdrawal < 1000:
        print("Minimum Balance Warning")

    else:
        print("Withdrawal Successful")
        account_balance = after_withdrawal
        print(f"Remaining balance: ₹{account_balance:.2f}")

    another_withdrawal = input(
        "Do you want to do another withdrawal? (yes/no): "
    )

    if another_withdrawal.lower() == "no":
        ATM = False

print("ATM session ended.")

#2

total = marks
average = total / 5

if s1 and s2 and s3 and s4 and s5 > 35:

    if  average >= 90 and 100:
        print("Grade A")

    elif average >= 75 and 89:
        print("Grade B")

    elif average >= 60 and 74:
        print("Grade C")

    elif average >= 50 and 59:
        print("Grade D")
    else:
        print("Grade E")

    print("You are scored more that 35")
else:
    print("You are failed")

#3
correct_username = "admin"
correct_password = "Python@123"

attempts = 0

while attempts < 3:
    user_name = input("Enter the username: ")
    password = input("Enter the password: ")

    if user_name == correct_username and password == correct_password:
        print("Login Successful")
        break

    else:
        attempts += 1
        print("Invalid Credentials")

        remaining_attempts = 3 - attempts

        if attempts == 3:
            print("Account Locked")
        else:
            print(f"Remaining attempts: {remaining_attempts}")