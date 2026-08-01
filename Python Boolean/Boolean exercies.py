# 1. Voting Eligibility
#
# Write a program that asks for:
#
# age
# citizenship status (True or False)
#
# Print:
#
# "Eligible to Vote"
# "Not Eligible to Vote"

# def vote(age,citizenship_status ):
#
#     if age >= 18 and citizenship_status:
#         print("Eligible to vote")
#     else:
#         print("Eligible to vote")
#
# vote(18, True)

age = int(input("Enter the age"))
has_license = input(f"Enter True or False")

def check(age, has_license):
    if age >= 18 and has_license:
        print("Can Drive")
    else:
        print("cannot Drive")


check(age, has_license)


