# Ask the user how many Fibonacci numbers they want
n = int(input("Enter number of terms: "))

# First two Fibonacci numbers
first = 0
second = 1

print("Fibonacci Series:")

for i in range(n):
    print(first, end=" ")

    # Calculate the next number
    next_number = first + second

    # Update values
    first = second
    second = next_number