#1
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")

#2
color = "red"
match color:
    case "red":
        print("stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")

#3
a = 10
b = 5
operator = "+"

match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)

choice = 2
match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("update")
    case 4:
        print("Delete")
    case _:
        print("Invalid choice")

month = 4

match month:
    if 1 month 12:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
    else:
        print("Invalid Month")

grade = "B"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Needs improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid grade")

option = 3
match option:
    case 1:
        print("Check Balance")
    case 2:
        print("Deposit")
    case 3:
        print("Withdraw")
    case 4:
        print("Exit")

animal = "dog"

match animal:
    case "dog":
        print("woof")
    case "cat":
        print("Meow")
    case "cow":
        print("Moo")
    case "lion":
        print("Roar")
    case _:
        print("Unknown animal")

day = "Saturday"

match day:
    case "Saturday" and "Sunday":
        print("Weekend")
    case "Monday":
        print("Weekday")
    case "Tuesday":
        print("Weekday")
    case "Wednesday":
        print("Weekday")
    case "Thuresday":
        print("Weekday")
    case "Friday":
        print("Weekday")
    case _:
        print("Invalid day")

number = 2

match number:
    case number = 1 , 2, 3:
        print("small")

    case number = 4, 5, 6:
        print("Medium")

    case number = 7, 8, 9, 10
        print("Large")

    case _:
        print("Out of range")






