def print_butterfly(size):
    for i in range(1, size + 1):
        print("*" * i + " " * (size - i) + " " * (size - i) + "*" * i)
    for i in range(size-1, 0, -1):
        print("*" * i + " " * (size - i) + " " * (size - i) + "*" * i)

print_butterfly(10)