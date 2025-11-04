# src/neighbors.py

def count_neighbors(grid, r, c, wrap=False):
    """
    Count the number of alive neighbors around a cell at (r, c).
    Supports wrapping edges if wrap=True.
    """
    if wrap:
        return _count_neighbors_wrap(grid, r, c)
    else:
        return _count_neighbors_nowrap(grid, r, c)


def _count_neighbors_nowrap(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                cnt += grid[rr][cc]
    return cnt


def _count_neighbors_wrap(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            rr = (r + dr) % rows
            cc = (c + dc) % cols
            cnt += grid[rr][cc]
    return cnt
