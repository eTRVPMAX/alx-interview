def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    Args:
        grid: 2d list of integers containing 0 (water) or 1 (land)
    Return:
        the perimeter of the island
    """
    
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check for water or grid boundary on all 4 sides
                if i == 0 or grid[i - 1][j] == 0:  # Top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
