import os                      
import sys                     
import time                    
import random                  
import argparse                
from copy import deepcopy      

ALIVE = "0"                    
DEAD = " "                     

def make_grid(rows, cols, alive_prob=0.2):           
    return [[1 if random.random() < alive_prob else 0 for _ in range(cols)] for _ in range(rows)]
    

def count_neighbors(grid, r, c, wrap):               
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

def step(grid, wrap=True):                            
    rows, cols = len(grid), len(grid[0])              
    new = [[0]*cols for _ in range(rows)]             
    for r in range(rows):                            
        for c in range(cols):                         
            n = count_neighbors(grid, r, c, wrap)    
            if grid[r][c] == 1:                      
                new[r][c] = 1 if n in (2, 3) else 0  
            else:
                new[r][c] = 1 if n == 3 else 0      
    return new                                        

def clear_screen():                                   
    os.system('cls' if os.name == 'nt' else 'clear')  

def print_grid(grid, generation=None):                
    clear_screen()                                    
    if generation is not None:                     
        print(f"Generation: {generation}")
    for row in grid:                                 
        print("".join(ALIVE if cell else DEAD for cell in row)) 

def run(rows=20, cols=60, alive_prob=0.2, steps=None, interval=0.1, wrap=True, seed=None):
   
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

if __name__ == "__main__":                            
    p = argparse.ArgumentParser(description="Conway's Game of Life (terminal)")
    p.add_argument("--rows", type=int, default=20)     
    p.add_argument("--cols", type=int, default=60)     
    p.add_argument("--prob", type=float, default=0.2, help="initial alive probability")
    p.add_argument("--steps", type=int, default=None, help="number of generations (ctrl-c to stop if omitted)")
    p.add_argument("--interval", type=float, default=0.12, help="seconds between generations")
    p.add_argument("--no-wrap", action="store_true", help="disable toroidal wrapping of edges")
    p.add_argument("--seed", type=int, default=None, help="random seed for reproducible starts")
    args = p.parse_args()                             

    run(rows=args.rows, cols=args.cols, alive_prob=args.prob, steps=args.steps,
        interval=args.interval, wrap=not args.no_wrap, seed=args.seed)
    
