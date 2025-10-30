import random
import time
from grid_generation_module import make_grid, print_grid
from step import step

def run(rows=None, cols=None, alive_prob=0.2, steps=None, interval=0.1, wrap=True, seed=None):
   
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