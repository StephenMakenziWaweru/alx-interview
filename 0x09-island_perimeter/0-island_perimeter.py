#!/usr/bin/python3
"""Island perimeter module"""


def island_perimeter(grid):
    """Returns the perimeter of an island described by grid"""
    perimeter = 0           # total perimeter of island

    # logic is to check if the cell is surrounded by water or land on either
    # of top, bottom, left, right sides
    # if either side is not water, then subtract 1 from cell_perimeter
    # then add remaining cell perimeter to perimeter - do for all cells
    for row_i, row in enumerate(grid):
        for col_i, col in enumerate(row):
            cell_perimeter = 0
            if col == 1:
                cell_perimeter = 4      # perimeter of each cell
                try:
                    if grid[row_i - 1][col_i] == 1:  # top
                        cell_perimeter -= 1
                except IndexError:
                    pass
                try:
                    if grid[row_i + 1][col_i] == 1:  # bottom
                        cell_perimeter -= 1
                except IndexError:
                    pass
                try:
                    if grid[row_i][col_i + 1] == 1:  # right
                        cell_perimeter -= 1
                except IndexError:
                    pass
                try:
                    if grid[row_i][col_i - 1] == 1:  # left
                        cell_perimeter -= 1
                except IndexError:
                    pass
            perimeter += cell_perimeter
    return perimeter
