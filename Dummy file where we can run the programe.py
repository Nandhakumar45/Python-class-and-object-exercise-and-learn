balance = 1000


def deposit():
    global balance
    balance = balance + 500


def withdraw():
    global balance
    balance = balance - 200


def show_balance():
    print(balance)

deposit()
withdraw()
show_balance()