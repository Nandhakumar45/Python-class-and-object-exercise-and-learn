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







