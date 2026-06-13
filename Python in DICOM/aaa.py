
def process_number(n):
    # Convert number to string to access digits
    n_str = str(n)
    if len(n_str) != 3:
        return "Please enter a three-digit number"

    # Extract digits
    first_digit = int(n_str[0])
    second_digit = int(n_str[1])
    third_digit = int(n_str[2])

    # Square the second digit
    second_digit_squared = second_digit ** 2

    # Combine them in the order: first digit, second digit squared, third digit
    result = f"{first_digit}, {second_digit_squared}, {third_digit}"
    return result


# Example usage
number = int(input("Enter a three-digit number: "))
output = process_number(number)
print(output)

