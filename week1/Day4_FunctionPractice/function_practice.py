def square(number):
    return number * number


def cube(number):
    return number * number * number


def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Factorial of 5:", factorial(5))
print("Simple Interest:", simple_interest(1000, 5, 2))