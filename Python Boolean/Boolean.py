# #Write a program that checks if a number is greater than 10 and prints True or False.
#
# num = 15
# print(num > 10)
#
#
# ## 2. (Easy) Even or Odd
# #Write a function `is_even(n)` that returns `True` if a number is even, `False` otherwise.
#
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(6))  # True
# print(is_even(5))  # False
#
# ## 3. (Easy) Boolean Conversion
# #Predict the output without running the code:
# #```python
# print(bool(0)) # True
# print(bool(-5))  #False
# print(bool(""))  # False
# print(bool("False")) # True
# print(bool([])) # True
#
# # Here's why:
# #
# # bool(0) → False — 0 is one of Python's "falsy" values (any zero number is falsy, regardless of sign).
# # bool(-5) → True — This trips people up! Any non-zero number is truthy, even negative numbers. Only 0 (and 0.0) is falsy.
# # bool("") → False ✅ — Empty string is falsy.
# # bool("False") → True ✅ — This is the sneaky one.
# # "False" is a non-empty string (it has characters in it), so it's truthy — Python doesn't look at what the string says, just whether it's empty or not.
# # bool([]) → False — Empty list is falsy, just like empty string. You need at least one item in the list for it to be truthy.
#
# ## 4. (Easy-Medium) Logical Operators
# #Write a function `can_vote(age, is_citizen)`
# #that returns `True` only if age >= 18 **and** is_citizen is `True`.
#
# def can_vote(age, is_citizen):
#     if age >= 18 and is_citizen == True:
#         return True
#     else:
#         return False
#
# print(can_vote(18, True))   # True
# print(can_vote(17, True))   # False
# print(can_vote(20, False))  # False
# print(can_vote(5, True))    # False
#
# def can_vote(age, is_citizen):
#     return age >= 18 and is_citizen
#
# print(can_vote(18, True))



## 5. (Medium) Multiple Conditions
# Write a function `is_valid_password(password)` that returns `True` only if:
# - Length is at least 8 characters
# - Contains at least one digit
# - Contains at least one uppercase letter

# def is_valid_password(password):
#     if len(password) < 8:
#         return False
#     if not any(char.isdigit() for char in password):
#         return False
#     if not any(char.isupper() for char in password):
#         return False
#     return True
#
# print(is_valid_password("Abcdefg1"))  # True
# print(is_valid_password("abcdefg1"))  # False (no uppercase)
# print(is_valid_password("ABCDEFG1"))  # True... wait, check: has digit, upper, len 8 -> True
#print(is_valid_password("short1A"))   # False (only 7 chars)























