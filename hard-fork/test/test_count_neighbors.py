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


def test_top_left_corner_counts_only_in_bounds_neighbors_when_no_wrap():
    """Without wrapping, corner cells ignore out-of-bounds neighbors."""
    grid = make_grid("""
        ***
        ...
        ...
    """)
    top_left_cell = (0, 0)
    assert count_neighbors(grid, *top_left_cell, wrap=False) == 1


def test_corners_are_neighbors_when_wrap_enabled():
    """With wrapping enabled, opposite corners are considered neighbors."""
    grid = make_grid("""
        *..
        ...
        ..*
    """)
    top_left_cell = (0, 0)
    assert count_neighbors(grid, *top_left_cell, wrap=True) == 1