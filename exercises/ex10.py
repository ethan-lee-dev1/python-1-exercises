def calculator():
    """comments"""
    num1 = input("Enter a number 1: ")
    num2 = input("Enter a number 2: ")
    if num1.isdigit() or num2.isdigit():
        print("Enter numbers!")
        return
    num1, num2 = float(num1), float(num2)
    operation = input ("(+, *, /, -): ")
    if operation == "+":
        print(num1 + num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    elif operation == "-":
        print(num1 - num2)
    else:
        print("wrong operation")