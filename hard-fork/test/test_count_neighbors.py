import pytest
from src.count_neighbors import count_neighbors

# Small visual helper for clarity
def make_grid(text):
    """Convert a multiline string of '.' and '*' into a grid of 0s and 1s."""
    lines = [line.strip() for line in text.strip().splitlines()]
    return [[1 if char == '*' else 0 for char in line] for line in lines]


def test_single_live_cell_has_no_neighbors():
    """A lone live cell should have zero neighbors."""
    grid = make_grid("""
        ...
        .*.
        ...
    """)
    center_cell = (1, 1)
    assert count_neighbors(grid, *center_cell) == 0
    
    

def test_fully_populated_grid_center_has_eight_neighbors():
    """In a fully populated 3×3 grid, the center cell has eight neighbors."""
    grid = make_grid("""
        ***
        ***
        ***
    """)
    center_cell = (1, 1)
    assert count_neighbors(grid, *center_cell) == 8