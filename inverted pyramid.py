def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + " *" * (2 * i - 1))


n = int(input(" Enter the length : "))
inverted_pyramid(n)