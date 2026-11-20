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