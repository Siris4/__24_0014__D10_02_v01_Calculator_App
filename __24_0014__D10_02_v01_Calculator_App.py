# Calculator app:
from __24_0014__D10_02_v01_Calculator_Logo import logo

print(logo)

#TODO 1: Create the functions

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

#TODO 2: Make the operational symbols as the Key for a Dictionary, and the Values as the function name
operations = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}

num1 = float(input("Choose the first number: "))


w = True
while w == True:
    for symbol in operations:
        print(symbol)

    operation_symbol = input("Please pick an operation from above: ")
    num2 = float(input("What's the second number?: "))

    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{int(num1)} {operation_symbol} {int(num2)} = {first_answer}")     #either remove ALL int() from this line to get more specific decimal places, when doing division

    repeat_calculation = input("Do you want to do another calculation with the last answer? (Y or N): ").upper()
    if repeat_calculation == "Y":
        num1 = first_answer
    elif repeat_calculation == "N":
        print("Have a great rest of your day doing your math manually!")
        w = False


 #next_answer = first_answer
    #2nd Iteration, using Input:
    # operation_symbol = input("Pick another operation: ")
    # next_number = float(input("What's the next number?: "))
    # calculation_function = operations[operation_symbol]
    #
    # second_answer = calculation_function(next_answer, next_number)
    # print(f"{int(next_answer)} {operation_symbol} {int(next_number)} = {int(next_number)}")


