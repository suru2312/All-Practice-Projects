import os

from art import logo

def operations(operation, first_number, second_number):
    result = 0
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Error: Division by zero!")
            return first_number
        result = first_number / second_number
    else:
        print("Wrong Input!")
        return first_number
    
    print(f"{first_number} {operation} {second_number} = {result}")
    return result


def calculator():
    loop = True
    should_continue = "-1"
    sum_of_ops = 0

    while loop:
        print(logo)
        if should_continue == "-1":
            f_num = float(input("What's the first number: "))
        else:
            f_num = sum_of_ops
            print(f"Continuing with: {sum_of_ops}")

        print("+\n-\n*\n/")
        ops = input("Pick an operation: ")
        s_num = float(input("What's the second number: "))

        sum_of_ops = operations(ops, f_num, s_num)

        should_continue = input(
            f"Type '0' to continue with {sum_of_ops}, "
            "or '1' to start a new calculation, "
            "or '2' to exit: "
        )

        if should_continue == "0":
            os.system("cls" if os.name == "nt" else "clear")
        elif should_continue == "1":
            os.system("cls" if os.name == "nt" else "clear")
            should_continue = "-1"
        elif should_continue == "2":
            loop = False
        else:
            print("Wrong Input! Restarting...")
            os.system("cls" if os.name == "nt" else "clear")
            should_continue = "-1"

calculator()