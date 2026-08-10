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