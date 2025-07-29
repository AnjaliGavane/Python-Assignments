def star_pattern(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

rows = int(input("Enter the number of rows for the pattern: "))
star_pattern(rows)
