# src/neighbors.py

def count_neighbors(grid, r, c, wrap):
    """
    Count the number of alive neighbors around a cell at (r, c).
    Supports wrapping edges if wrap=True.
    """
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if wrap:
                rr %= rows
                cc %= cols
                cnt += grid[rr][cc]
            else:
                if 0 <= rr < rows and 0 <= cc < cols:
                    cnt += grid[rr][cc]
    return cnt
