import copy
import pytest

from step import step

#next step tests
def test_block_stable():
    # 2x2 block should remain unchanged (still life)
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    new = step(grid, wrap=False)
    assert new == grid


def test_blinker_oscillator():
    # Vertical blinker becomes horizontal after one step and back after two
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    after1 = step(grid, wrap=False)
    # Expect horizontal line in the middle row
    expected1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert after1 == expected1
    after2 = step(after1, wrap=False)
    assert after2 == grid


def test_empty_grid_unchanged():
    grid = [[0 for _ in range(4)] for __ in range(3)]
    new = step(grid, wrap=False)
    assert new == grid


def test_full_grid_edges_die():
    # In a full grid with no wrapping:
    # - Corner cells have 3 neighbors (survive)
    # - Edge cells have 5 neighbors (die)
    # - Internal cells have 8 neighbors (die)
    grid = [[1 for _ in range(4)] for __ in range(4)]
    new = step(grid, wrap=False)
    # Corner cells should survive (3 neighbors)
    assert new[0][0] == 1  # Corner cells survive
    assert new[0][3] == 1
    assert new[3][0] == 1
    assert new[3][3] == 1
    # Edge and internal cells should die (>3 neighbors)
    assert new[1][1] == 0  # Internal cell dies
    assert new[0][1] == 0  # Edge cell dies


def test_1x1_grid_no_wrap_live_dies_and_dead_stays_dead():
    grid_live = [[1]]
    grid_dead = [[0]]
    assert step(grid_live, wrap=False) == [[0]]
    assert step(grid_dead, wrap=False) == [[0]]


def test_1x1_grid_with_wrap_live_dies_and_dead_stays_dead():
    # With wrapping the single cell counts as its own neighbor multiple times
    assert step([[1]], wrap=True) == [[0]]
    assert step([[0]], wrap=True) == [[0]]


def test_preserve_shape_and_values():
    # Ensure the output grid has same shape and only 0/1 values
    grid = [
        [0, 1, 0],
        [1, 0, 1],
    ]
    out = step(grid, wrap=False)
    assert len(out) == len(grid)
    assert all(len(row) == len(grid[0]) for row in out)
    assert all(cell in (0, 1) for row in out for cell in row)

#Wrap testing
def test_wrap_edge_survival():
    # Test cell survival at edges with wrapping
    grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    # With wrap=True, corners see each other and form a stable pattern
    new = step(grid, wrap=True)
    # Each corner has 3 neighbors when wrapped (2 adjacent + 1 diagonal through wrap)
    assert new[0][0] == 1  # Corners survive with 3 neighbors each
    assert new[0][2] == 1
    assert new[2][0] == 1
    assert new[2][2] == 1


def test_wrap_birth():
    # Test cell birth at edges with wrapping
    grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]
    # With wrap=True, cells at edges can be born due to wrapped neighbors
    new = step(grid, wrap=True)
    assert new[0][2] == 1  # Top-right remains/born due to 3 neighbors when wrapped


def test_wrap_vs_no_wrap():
    # Test same grid with and without wrapping to show difference
    grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    wrapped = step(grid, wrap=True)
    unwrapped = step(grid, wrap=False)
    assert wrapped != unwrapped  # Results should differ due to different neighbor counts


def test_wrap_horizontal_line():
    # Test wrapping behavior with a horizontal line pattern
    grid = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    new = step(grid, wrap=True)
    # With wrapping, each cell in the line has 2 neighbors,
    # and cells above/below get 3 neighbors through wrapping
    expected = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert new == expected


def test_wrap_vertical_line():
    # Test wrapping behavior with a vertical line pattern
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    new = step(grid, wrap=True)
    # With wrapping, each middle cell has 2 neighbors (sides) plus 1 through wrap
    # Cells to left/right get 3 neighbors through wrapping
    expected = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert new == expected
