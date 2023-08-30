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
            if grid[row][col] == 1:
                perimeter += 4  # Each land cell contributes 4 to perimeter

                # Check adjacent cells and subtract 1 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
