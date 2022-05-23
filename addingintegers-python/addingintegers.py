# python program that adds 2 numbers together and output the result on your terminal

# User inputs two numbers
# Convert inputs to integers. Not float because the assignment title on adding integers
try:
    num1 = int(input("Enter your first intger: "))
    num2 = int(input("Enter your second integer: "))

# Add both variables and save in a new variable, "addition", then print.
    addition = num1 + num2
    print(addition)
#print ValueError if input is not a number
except ValueError:
    print("Invalid input! Enter an integer.")