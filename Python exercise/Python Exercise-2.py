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
customer_name = input("Enter customer name: ")
unit_consumed = int(input("Enter units consumed: "))

if unit_consumed <= 0:
    print("Invalid input. Units must be greater than 0.")

else:

    if unit_consumed <= 100:
        Energy_Charge = unit_consumed * 2

    elif unit_consumed <= 200:
        Energy_Charge = (100 * 2) + ((unit_consumed - 100) * 3)

    else:
        Energy_Charge = (100 * 2) + (100 * 3) + ((unit_consumed - 200) * 5)

    if unit_consumed > 300:
        surcharge = Energy_Charge * 5 / 100
    else:
        surcharge = 0

    TotalBill = Energy_Charge + surcharge

    print("===== ELECTRICITY BILL =====")
    print(f"Customer Name : {customer_name}")
    print(f"Units         : {unit_consumed}")
    print(f"Energy Charge : {Energy_Charge:.2f}")
    print(f"Surcharge     : {surcharge:.2f}")
    print(f"Total Bill    : {TotalBill:.2f}")

#8
product_name = input("Enter product name: ")
available_stock = int(input("Enter available stock: "))
reorder_level = int(input("Enter reorder level: "))

if "medical" in product_name.lower():
    product_type = "Medical Product"
else:
    product_type = "Regular Product"

if available_stock == 0:
    stock_status = "Out of Stock"
elif available_stock < reorder_level:
    stock_status = "Low Stock"
elif available_stock == reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Stock Available"

print("===== INVENTORY REPORT =====")
print(f"Product Name   : {product_name}")
print(f"Product Type   : {product_type}")
print(f"Available Stock: {available_stock}")
print(f"Reorder Level : {reorder_level}")
print(f"Stock Status  : {stock_status}")

#9
employee_name = input("Enter the employee name: ")

score1 = int(input("Enter first performance score: "))
score2 = int(input("Enter second performance score: "))
score3 = int(input("Enter third performance score: "))

# Multiple assignment
s1, s2, s3 = score1, score2, score3

total = s1 + s2 + s3
average = total / 3

# Evaluate performance grade
if average >= 90:
    grade = "Excellent"
elif average >= 75:
    grade = "Good"
elif average >= 60:
    grade = "Average"
else:
    grade = "Needs Improvement"

# Nested if to determine final status
if s1 >= 40 and s2 >= 40 and s3 >= 40:
    if average >= 60:
        status = "Normal"
    else:
        status = "Needs Improvement"
else:
    status = "Performance Review Required"

print("===== EMPLOYEE PERFORMANCE =====")
print(f"Employee Name: {employee_name}")
print(f"Score 1      : {s1}")
print(f"Score 2      : {s2}")
print(f"Score 3      : {s3}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Result       : {status}")

#10
project_name = input("Enter project name: ").upper()
tester_name = input("Enter tester name: ")
total_test_case = int(input("Enter total test cases: "))

passed = int(input("Enter passed test cases: "))
failed = int(input("Enter failed test cases: "))
blocked = int(input("Enter blocked test cases: "))
non_executed = int(input("Enter not-executed test cases: "))

reviewer = None

if reviewer is None:
    reviewer = "Not Assigned"

# Validation
report_valid = (
    total_test_case > 0
    and passed >= 0
    and failed >= 0
    and blocked >= 0
    and non_executed >= 0
    and (passed + failed + blocked + non_executed) == total_test_case
)

if report_valid:

    executed_test_cases = passed + failed + blocked

    execution_percentage = (executed_test_cases / total_test_case) * 100

    if executed_test_cases > 0:
        pass_percentage = (passed / executed_test_cases) * 100
        failure_percentage = (failed / executed_test_cases) * 100
    else:
        pass_percentage = 0.0
        failure_percentage = 0.0

    # Execution status
    if execution_percentage >= 95:
        execution_status = "Excellent Execution"
    elif execution_percentage >= 80:
        execution_status = "Good Execution"
    else:
        execution_status = "Poor Execution"

    # Final status
    if failure_percentage > 10:
        final_status = "Attention Required"
    else:
        final_status = execution_status

    print("========== QA PROJECT DASHBOARD ==========")

    print("Project Name      : {}".format(project_name))
    print("Tester Name       : {}".format(tester_name))
    print("Reviewer          : {}".format(reviewer))
    print("Total Test Cases  : {}".format(total_test_case))
    print("Passed           : {}".format(passed))
    print("Failed           : {}".format(failed))
    print("Blocked          : {}".format(blocked))
    print("Not Executed      : {}".format(non_executed))
    print("---------------------------------------")
    print("Execution         : {:.2f}%".format(execution_percentage))
    print("Pass Percentage   : {:.2f}%".format(pass_percentage))
    print("Failure Percentage: {:.2f}%".format(failure_percentage))
    print("Execution Status : {}".format(execution_status))
    print("Final Status     : {}".format(final_status))
    print("Report Valid     : {}".format(report_valid))

else:
    print("Invalid test case counts!")
    print("Report Valid: {}".format(report_valid))

















