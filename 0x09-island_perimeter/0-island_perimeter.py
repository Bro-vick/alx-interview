#!/usr/bin/python3
"""Island Perimeter solution"""


def island_perimeter(grid):
    """This Returns the perimeter of the island """
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
