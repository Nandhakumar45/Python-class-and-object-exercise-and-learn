#1
i = 1

while i<=5:
    j = 1
    while j <= 5:
        print(j , end = "")
        j += 1
    i += 1
    print()

#2
i = 1

while i<=5:
    j = 1
    while j <= 5:
        print( "*", end = "")
        j += 1
    i += 1
    print()

#3
i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(j, end=" ")
        j += 1

    print()
    i += 1

#4
i = 2
while i<=5:
    j = 1
    while j <= 10:
        print(i,"*",j , "=" , i * j )
        j += 1
    i += 1
    print("************")
    print()

#5
i = 5

while i >= 1:
    j = 5

    while j >= 6 - i:
        print(j, end=" ")
        j -= 1

    print()
    i -= 1

#6
i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(i, end=" ")
        j += 1

    print()
    i += 1

#7
i = 1

while i <= 5:
    j = 1

    while j <= 5 - i:
        print(" ", end=" ")

        j += 1

    k = 1

    while k <= i:
        print("*", end=" ")
        k += 1

    print()
    i += 1

#8
i = 1

while i <= 5:
    j = 1

    while j <= 5:

        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")

        j += 1

    print()
    i += 1

#9
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1

    print()
    i += 1

#10
i = 1

while i <= 50:
    j = 1

    while j <= 1:

        if i % 2 == 0 and i % 3 == 0:
            print(i)

        j += 1

    i += 1

