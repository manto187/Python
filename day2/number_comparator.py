def number_comparison_tool():
    """
    A simple tool to compare three numbers using nested if conditions,
    logical operators, and comparison operators.
    """
    print("Welcome to the Number Comparison Tool")
    print("Please enter three numbers to compare.")

    try:
        # Taking input from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        print(f"\nComparing {num1}, {num2}, and {num3}...")

        # Feature: Check if all numbers are equal using Logical Operators
        if num1 == num2 and num2 == num3:
            print("Output: All three numbers are equal.")
        else:
            # Nested If conditions to find the largest number
            if num1 >= num2:
                # If num1 is greater or equal to num2, we simplify the comparison to num1 vs num3
                if num1 >= num3:
                    largest = num1
                else:
                    largest = num3
            else:
                # If num2 is greater than num1, we compare num2 vs num3
                if num2 >= num3:
                    largest = num2
                else:
                    largest = num3
            
            print(f"Output: The largest number is {largest}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    number_comparison_tool()
