#1
employee_name = "Nandha"
employee_id = 101

basic_salary = 45000

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da

print("========== EMPLOYEE REPORT ==========")
print(f"Employee Name : {employee_name}")
print(f"Employee ID   : {employee_id}")
print(f"Basic Salary  : {basic_salary:.2f}")
print(f"HRA (20%)     : {hra:.2f}")
print(f"DA (10%)      : {da:.2f}")
print(f"Gross Salary  : {gross_salary:.2f}")
print("===================================")

#2
Tamil = 85
English = 90
Maths = 95
Science = 88
Social = 92

Total = Tamil + English + Maths + Science + Social
average = Total / 5
percentage = (Total / 500)  * 100
print("==============STUDENT MARKSHEET====================")
print(f"Tamil       : {Tamil}")
print(f"English     : {English}")
print(f"Maths       : {Maths}")
print(f"Science     : {Science}")
print(f"Social      : {Social}")
print("----------------------------------------------------")
print(f"Total Marks : {Total}")
print(f"Average     : {average}")
print(f"Percentage  : {percentage}%")
print("==================================================")

#3
Product = "Laptop"
Price = 65000.00
Quantity = 2
Discount = 10
GST = 18

Subtotal = Price * Quantity
Discount_Amount = Subtotal * (Discount / 100)
Taxable_Amount = Subtotal - Discount_Amount
GST_Amount = Taxable_Amount * (GST / 100)
Final_Amount = Taxable_Amount + GST_Amount
print("========== SHOPPING BILL ==========")
print(f"Product :{Product}")
print(f"Price    :{Price}")
print(f"Quantity  :{Quantity}")
print(f"Subtotal  :{Subtotal}")
print(f"Discount (10%): {Discount_Amount}")
print(f"Tabable Amount: {Taxable_Amount}")
print(f"GST (18%): {GST_Amount}")
print(f"Final Amount: {Final_Amount}")
print("======================================")

#4
Project = "Cardiology Workflow"
Total_Test_Cases = 250
Passed = 210
Failed = 20
Blocked = 10
Not_Executed = 10
Execution = (Passed + Failed + Blocked) / Total_Test_Cases * 100
Pass = Passed / Execution * 100
print("========== TEST EXECUTION REPORT ==========")
print("Project          :", Project)
print("Total Test Cases :", Total_Test_Cases)
print("Passed           :", Passed)
print("Failed           :", Failed)
print("Blocked          :", Blocked)
print("Not Executed     :", Not_Executed)
print("-------------------------------------------")
print(f"Execution %      : {Execution:.2f}")
print(f"Pass %           : {Pass:.2f}")


#5
















