num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))


for row in range(num_rows):
    
    if row == 0 or row == num_rows - 1:
        print("*" * num_cols)
    else:
        
        print("*" + " " * (num_cols - 2) + "*")