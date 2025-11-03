import os

def clear_screen():                                   
    os.system('cls' if os.name == 'nt' else 'clear')  

def print_grid(grid, generation=None):                
    clear_screen()                                    
    if generation is not None:                     
        print(f"Generation: {generation}")
    for row in grid:                                 
        print("".join('*' if cell else '.' for cell in row)) 
