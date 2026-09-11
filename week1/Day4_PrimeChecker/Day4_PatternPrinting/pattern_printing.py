print("Pattern 1")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nPattern 2")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nPattern 3")

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()