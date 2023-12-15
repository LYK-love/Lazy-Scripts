# Define the size of the square table
size = 7  # You can change this to the desired size

# Print the column headers
header_row = "     |"
for col_num in range(1, size + 1):
    header_row += f" {col_num:^5} |"
print(header_row)
print("-" * len(header_row))

# Generate and print the square table with row numbers in the first column and square grid
for row_num in range(1, size + 1):
    row = f" {row_num:2d}  |"
    for col_num in range(1, size + 1):
        fraction = f"{row_num}/{col_num}"
        cell = f"{fraction:^6}"
        row += f" {cell} |"
    print(row)
    print("-" * len(header_row))
