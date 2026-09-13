"""Write a Python program that:numbers=[10,25,40,15,30]

Finds the largest number manually using a loop
Finds the smallest number manually using a loop
Calculates the sum
Calculates the average
Do not use max() or min()"""

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 25, 40, 15, 30]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number


total = calculate_sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)