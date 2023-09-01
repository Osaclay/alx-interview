#!/usr/bin/python3
"""
0-island_perimeter module
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The island grid.

    Returns:
        int: The perimeter of the island.
    """

    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (grid[row][col] == 1):
                if (row <= 0 or grid[row - 1][col] == 0):
                    perimeter += 1
                if (row >= len(grid) - 1 or grid[row + 1][col] == 0):
                    perimeter += 1
                if (col <= 0 or grid[row][col - 1] == 0):
                    perimeter += 1
                if (col >= len(grid[row]) - 1 or grid[row][col + 1] == 0):
                    perimeter += 1
    return perimeter
