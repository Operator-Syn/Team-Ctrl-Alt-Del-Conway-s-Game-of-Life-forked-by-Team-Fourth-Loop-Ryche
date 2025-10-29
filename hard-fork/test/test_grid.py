from src.grid_generation_module import make_grid

def test_default_make_grid():
    rows, cols = 10, 10
    grid = make_grid(rows, cols, alive_prob=0.5)
    assert len(grid) == rows
    assert all(len(row) == cols for row in grid)
    assert all(cell in (0, 1) for row in grid for cell in row)

def test_make_grid_all_alive():
    rows, cols = 5, 5
    grid = make_grid(rows, cols, alive_prob=1.0)
    assert all(cell == 1 for row in grid for cell in row)