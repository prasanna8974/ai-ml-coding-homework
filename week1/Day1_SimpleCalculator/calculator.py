def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operator."


print("Simple Calculator")
print("-----------------")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

result = calculator(num1, num2, operator)

print("Result:", result)