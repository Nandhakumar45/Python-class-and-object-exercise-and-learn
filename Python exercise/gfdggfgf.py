for outer in range(1, 6):
    for inner in range(1, 6):
        if outer % 2 == 0:
            if inner % 2 == 0:
                print(outer, inner , "Both the outer and inner are even")
            else:
                print(outer, inner, "outer is even and inner is odd")
        else:
            if inner % 2 == 0:
                print(outer, inner, "Outer is odd and inner is even")
            else:
                print(outer, inner, "Both are odd")