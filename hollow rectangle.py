def hollow_square(rows):
    for i in range(rows):
            for j in range(columns):                
                if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                    print("*", end=" ")
                else:
                     print(" ", end=" ")
            print()
rows = int(input("Enter the number of rows: "))
hollow_square(rows)
