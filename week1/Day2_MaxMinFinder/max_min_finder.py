def find_max_min(numbers):
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    return largest, smallest


numbers = [25, 10, 45, 5, 30, 60]

largest, smallest = find_max_min(numbers)

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)