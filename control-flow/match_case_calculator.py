num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

opration = input("Choose the operation (+, -, *, /):.")

match opration:
    case "+":
        result = num1 + num2
        print(f"The result is:{result}.")
    case "-":
        result = num1 - num2
        print(f"The result is:{result}.")
    case "*":
        result = num1 * num2
        print(f"The result is:{result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, or /.")
