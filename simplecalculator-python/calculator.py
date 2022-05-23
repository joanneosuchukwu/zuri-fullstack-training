# Task Title: Simple CLI Calculator
# Write a Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations. It should accept user input

# from __future__ import division


print("Simple CLI Calculator, select operation: ")
print("+")
print("-")
print("/")
print("*")
print("%")

while True:
    # user inputs operator
    operation = str(input("Enter operation choice: "))

    # confirm that user operation entry is within the list of valid operators
    op_lst = ["+", "-", "/", "*", "%"]
    if operation in op_lst:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                # perform addition
                result = num1 + num2
                print(f"Answer is % {result}")

            elif operation == "-":
                # perform subtraction
                result = num1 - num2
                print(f"Answer is % {result}")

            elif operation == "/":
                # perform division
                result = num1 / num2
                print(f"Answer is % {result}")

            elif operation == "*":
                # perform multiplication
                result = num1 * num2
                print(f"Answer is % {result}")

            elif operation == "%":
                # perform modulus
                result = num1 % num2
                print(f"Answer is % {result}")

            else:
                print("Invalid")

        except:
            print("Invalid Entry")

        # check if user wants another calculation
        # break while loop if "no"
        next_calc = input("Perform next calculation? yes/no: ")
        if next_calc == "no":
            break

    else:
        print("Invalid entry! Enter valid operation")

        # check if user wants another calculation
        # break while loop if "no"
        new_operator = input("Select another operator? yes/no: ")
        if new_operator == "no":
            break