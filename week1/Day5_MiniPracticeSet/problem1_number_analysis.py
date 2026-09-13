"""Write a Python program that asks the user to enter one integer. Create a function that determines:

Whether the number is Positive, Negative, or Zero
Whether the number is Even or Odd
Display both results."""


def analyze_number(number):
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    if number % 2 == 0:
        number_type = "Even"
    else:
        number_type = "Odd"

    return sign, number_type


number = int(input("Enter a number: "))

sign, number_type = analyze_number(number)

print("Number:", number)
print("Classification:", sign)
print("Type:", number_type)