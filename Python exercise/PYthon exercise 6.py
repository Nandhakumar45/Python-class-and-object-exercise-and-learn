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