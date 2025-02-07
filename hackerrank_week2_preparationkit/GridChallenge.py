def gridChallenge(grid):
    # Write your code here
    # sort the array element
    # compare the the a[0] < a[1]
    for i in range(len(grid)):
        sorted_row = sorted(grid[i])  # Sort the row
        grid[i] = ''.join(sorted_row)  # Replace the row with the sorted one

        # Check each column for alphabetical order
    col_count = len(grid[0])  # Number of columns
    row_count = len(grid)  # Number of rows

    for col in range(col_count):  # Loop through each column
        for row in range(row_count - 1):  # Compare each row with the one below it
            if grid[row][col] > grid[row + 1][col]:  # If the column is not sorted
                return "NO"

    return "YES"

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

gridChallenge(grid)

grid = ['abc', 'lmp', 'qrt']
print(gridChallenge(grid))