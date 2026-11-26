'''
    This exercise talk about the nested for and nested if condition
'''
'''
Beginner level
Exercise 1 – Number comparison

Write a program:
1. Outer loop runs from 1 to 5.
2. Inner loop runs from 1 to 5.
3. If the outer number is greater than the inner number:
   - Check whether the outer number is even.
   - If even, print Greater and Even.
   - Otherwise, print Greater and Odd.
4. Otherwise, print Smaller or Equal.
'''
for outer in range(1, 6):
    for inner in range(1, 6):
        if outer > inner:
            if outer %2 == 0:
                print(outer, inner , "Greater and even")
            else:
                print(outer, inner ,"Greater and odd")
        else:
            print(outer, inner , "smaller and equal")

'''
Outer loop runs from 1 to 5.
Inner loop runs from 1 to 5.
If the outer number is even:
- If the inner number is even, print Both Even.
- Otherwise, print Outer Even, Inner Odd.
Otherwise:
- If the inner number is even, print Outer Odd, Inner Even.
- Otherwise, print Both Odd.
'''

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

'''
1. Outer loop runs from 1 to 5.
2. Inner loop runs from 1 to 10.
3. If the inner number is greater than 5:
   - If the outer number is greater than 3, print `Both Conditions Satisfied`.
   - Otherwise, print `Only Inner Condition Satisfied`.
4. Otherwise, print `Inner Number Below Range`.
'''
for outer in range(1, 6):
    for inner in range(1, 11):
        if inner > 5:
            if outer > 3:
                print(outer, inner, "Both conditions satisfied")
            else:
                print(outer, inner, "Only inner condition satisfied")
        else:
            print(outer, inner, "Number are below range")

'''
1. Outer loop runs from 1 to 5.
2. Inner loop runs from 1 to 10.
3. Calculate multiplication of both numbers.
4. If the result is greater than 10:
   - If the result is divisible by 2, print `Greater than 10 and Even`.
   - Otherwise, print `Greater than 10 and Odd`.
5. Otherwise, print `Result is 10 or Below`.
'''
for outer in range(1, 6):
    for inner in range(1, 11):
        result = outer * inner

        if result > 10:

            if result % 2 == 0:
                print(result, "Greater than 10  and even")

            else:
                print(result, "Greater than 10 and odd")

        else:
            print(result, "Result is 10 or Below")

'''
1. Outer loop runs from 2 to 10.
2. Inner loop runs from 2 to the outer number.
3. Check whether the outer number is divisible by the inner number.
4. If divisible:
   - Check whether both numbers are equal.
   - If equal, identify it as a possible prime number.
   - Otherwise, identify it as a composite number.
5. Avoid printing the same number multiple times.
'''
for outer in range(2, 11):
    is_prime = True

    for inner in range(2, outer):
        if outer % inner == 0:
            print(outer, "Composite Number")
            is_prime = False
            break

    if is_prime:
        print(outer, "Possible Prime Number")

'''
1. Outer loop runs from 1 to 5.
2. Inner loop runs from 1 to 5.
3. If the inner number is less than or equal to the outer number:
   - If the inner number is even, print `E`.
   - Otherwise, print `O`.
4. Otherwise, print `-`.
'''
for outer in range(1, 6):
    for inner in range(1, 6):
        if inner <= outer:
            if inner % 2 == 0:
                print("E", end = "")

            else:
                print("O", end = "")
        else:
            print("-", end = "")
    print()
