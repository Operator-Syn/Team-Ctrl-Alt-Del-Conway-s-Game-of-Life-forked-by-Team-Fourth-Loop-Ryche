import pytest
from src.count_neighbors import count_neighbors

def test_no_neighbors():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert count_neighbors(grid, 1, 1, wrap=False) == 0
