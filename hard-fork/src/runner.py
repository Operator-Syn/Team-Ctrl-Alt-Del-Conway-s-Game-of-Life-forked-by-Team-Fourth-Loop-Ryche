import random
import time
from grid_generation import make_grid
from step import step
from display import print_grid

def run(rows=20, cols=20, alive_prob=0.2, steps=None, interval=0.1, wrap=False, seed=None):
    """Run Conway's Game of Life simulation.
    
    Args:
        rows (int): Number of rows in the grid
        cols (int): Number of columns in the grid
        alive_prob (float): Probability of a cell being alive initially (0.0 to 1.0)
        steps (int, optional): Number of generations to run. None for infinite.
        interval (float): Time between generations in seconds
        wrap (bool): Whether the grid wraps around at edges
        seed (int, optional): Random seed for reproducibility
    
    Returns:
        list: The final state of the grid
    """
    if not (0.0 <= alive_prob <= 1.0):
        raise ValueError("alive_prob must be between 0.0 and 1.0")
    
    if seed is not None:
        random.seed(seed)
    
    grid = make_grid(rows, cols, alive_prob)
    gen = 0
    
    try:
        while True:
            print_grid(grid, gen)
            time.sleep(interval)
            grid = step(grid, wrap)
            gen += 1
            if steps is not None and gen >= steps:
                break
    except KeyboardInterrupt:
        print("\nStopped by user.")
    
    return grid

if __name__ == "__main__":
    run()