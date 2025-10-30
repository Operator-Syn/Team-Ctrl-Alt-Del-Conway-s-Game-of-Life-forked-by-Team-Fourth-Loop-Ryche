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