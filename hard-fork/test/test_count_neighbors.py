import pytest
from src.count_neighbors import count_neighbors

def test_no_neighbors():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert count_neighbors(grid, 1, 1, wrap=False) == 0

def test_full_neighbors():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    # The center cell should have 8 neighbors
    assert count_neighbors(grid, 1, 1, wrap=False) == 8

def test_edge_no_wrap():
    grid = [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # top-left corner (0,0) — only 1 neighbor (0,1)
    assert count_neighbors(grid, 0, 0, wrap=False) == 1
