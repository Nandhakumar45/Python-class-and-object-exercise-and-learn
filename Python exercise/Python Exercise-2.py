#1
employee_name = input("Enter the employee name:")
employee_ID   = input("Enter the employee_ID:")
salary  = input("Enter the basis salary:")
basic_salary  = float(salary)
HRA = basic_salary * 20 / 100
DA = basic_salary * 10 / 100
Gross_Salary = basic_salary + HRA + DA
Annual_Salary = Gross_Salary * 12

print("===== EMPLOYEE SALARY REPORT =====")
print("Employee Name: ".format(employee_name))
print("Employee ID  : ".format(employee_ID))
print(f"Basis Salary :.{basic_salary:.2f}")
print(f"Basis Salary :.{HRA:2f}")
print(f"Basis Salary :.{DA:2f}")
print(f"Basis Salary :.{Gross_Salary:2f}")
print(f"Basis Salary :.{Annual_Salary:2f}")


#2
student_name = input("Enter the student name:")
s1 = int(input("Enter first subject mark:"))
s2 = int(input("Enter second subject mark:"))
s3 = int(input("Enter third subject mark:"))
s4 = int(input("Enter fourth subject mark:"))
s5 = int(input("Enter fifth subject mark:"))

total = s1 + s2 + s3 + s4 + s5
average = total / 5

if s1 and s2 and s3 and s4 and s5 >= 35:
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"

    result = "Passed"

else:
    grade = "Fail"
    result = "Failed"

print("===== STUDENT MARKSHEET =====")
print(f"Student Name: {student_name}")
print(f"Total Marks : {total}")
print(f"Average     : {average:.2f}")
print(f"Grade       : {grade}")
print(f"Result      : {result}")


#3
project = input("Enter the project name:")
total_testcase = int(input("Enter the total number of test case:"))
passed = int(input("Enter the passed test case:"))
failed = int(input("Enter the failed test case:"))
blocked = int(input("Enter the blocked test case:"))
non_executed = int(input("Non executed test case:"))

executed = passed + failed + blocked
valid = passed + failed + blocked + non_executed == total_testcase
execution_Percentage = (executed / total_testcase) * 100
pass_Percentage = (passed / executed) * 100

if failed > 20:
    status = "High Failure RATE"
else:
    status = "Valid"

print("===== TEST EXECUTION REPORT =====")
print(f"Project          : {project}")
print(f"Total Test case  : {total_testcase}")
print(f"passed  : {passed}")
print(f"failed  : {failed}")
print(f"blocked  : {blocked}")
print(f"non_executed  : {non_executed}")
print(f"execution_Percentage  : {execution_Percentage:.2f}")
print(f"pass_Percentage  : {pass_Percentage:.2f}")
print(f"status  : {status}")

#4
Product = input("Enter a product name:")
quantity = int(input("Enter how many quantity need:"))
unit_price = int(input("Enter a unit price:"))

sub_total = quantity * unit_price

if sub_total >= 10000:
    discount = sub_total * 15 / 100
elif sub_total >= 5000:
    discount = sub_total * 10 / 100
elif sub_total >= 2000:
    discount = sub_total * 5 / 100
else:
    print("No discount")

final_amount = sub_total - discount

print("===== SHOPPING BILL =====")
print(f"Procut       : {Product.upper()}")
print(f"Quantity     : {quantity}")
print(f"unit_price   : {unit_price:.2f}")
print(f"Subtotal     : {sub_total:.2f}")
print(f"Discount     : {discount:.2f}")
print(f"final_amount : {final_amount:.2f}")


#5
name = input("Enter your name: ")
age = int(input("Enter your age: "))
balance = float(input("Enter your account balance: "))

employment_input = input("Are you employed (yes/no): ")
employed = employment_input.lower() == "yes"   # Boolean variable

reference_value = None

if age >= 21 and balance >= 50000 and employed:
    loan_eligible = "Yes"
else:
    loan_eligible = "No"

print("===== BANK ELIGIBILITY =====")
print(f"Customer Name : {name}")
print(f"Age           : {age}")
print(f"Balance       : {balance:.2f}")
print(f"Employment    : {employed}")
print(f"Loan Eligible : {loan_eligible}")

if reference_value is None:
    print("Reference Value : None")

#6
username = input("Enter username: ").strip().lower()
password = input("Enter password: ").strip()

username_valid = len(username) >= 5

password_valid = (
    ("@" in password or "#" in password)
    and password[0].isupper()
)

if username_valid and password_valid:
    final_status = "ACCEPTED"
else:
    final_status = "REJECTED"

print("===== LOGIN VALIDATION =====")
print(f"Username       : {username}")
print(f"Username Valid : {username_valid}")
print(f"Password Valid : {password_valid}")
print(f"Final Status   : {final_status}")


#7
customer_name = input("Enter a customer name")
unit_consumed = int(input("Enter a unit consumed"))

if unit_consumed >= 100:
    Energy_Charge = unit_consumed * 2

elif unit_consumed >= 101 and unit_consumed >= 200:
    Energy_Charge = unit_consumed * 3

elif unit_consumed >= 201 and unit_consumed >= 300:
    Energy_Charge = unit_consumed * 5






















