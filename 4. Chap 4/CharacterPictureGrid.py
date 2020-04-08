grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def print_grid(grid):
    number_rows = len(grid)
    number_cols = len(grid[0])

    for cols in range(number_cols):
        for rows in range(number_rows):
            print(grid[rows][cols], end = '')
        print()
if __name__ == "__main__":
    print_grid(grid)
        
