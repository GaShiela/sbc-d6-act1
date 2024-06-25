def print_pattern(rows):

    for i in range(rows, 1, -1):
        print("*" * i)

    print("*" + " " *(rows -2) + "*")

    for x in range(2, rows + 1):
        print("*" * x) 

rows = int(input("Rows: "))

print_pattern(rows)