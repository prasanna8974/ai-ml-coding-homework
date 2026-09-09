def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    result = check_even_odd(number)
    print(f"{number} is {result}.")