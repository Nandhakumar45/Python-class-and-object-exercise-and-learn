while True:
    try:
        pin = int(input("Enter your PIN: "))

        if pin == 1234:
            print("PIN is correct")
        else:
            raise ValueError("Incorrect PIN")

    except ValueError:
        print("Invalid PIN. Please try again.")

    else:
        print("Welcome to your account")
        break

    finally:
        print("ATM session checked")