import random
import time
from grid_generation import make_grid
from step import step
from display import print_grid

def run(grid=None, rows=20, cols=20, alive_prob=0.2, steps=None, interval=0.1, wrap=False, seed=None):
    """Run Conway's Game of Life simulation.
    
    Args:
        grid (list, optional): Existing grid to use. If None, a new grid will be created.
        rows (int): Number of rows in the grid (used only if grid=None)
        cols (int): Number of columns in the grid (used only if grid=None)
        alive_prob (float): Probability of a cell being alive initially (used only if grid=None)
        steps (int, optional): Number of generations to run. None for infinite.
        interval (float): Time between generations in seconds
        wrap (bool): Whether the grid wraps around at edges
        seed (int, optional): Random seed for reproducibility
    
    Returns:
        list: The final state of the grid
    """
    if grid is None:
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


def get_integer_input(prompt, min_value=None, max_value=None):
    """Helper function to get validated integer input."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def get_float_input(prompt, min_value=None, max_value=None):
    """Helper function to get validated float input."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def toggle_cell(grid, row, col):
    """Toggle the state of a cell between alive and dead."""
    grid[row][col] = 1 - grid[row][col]  # Toggle between 0 and 1
    return grid

def edit_grid(grid, settings):
    """Edit the grid by manually setting cells."""
    if grid is None:
        grid = make_grid(settings['rows'], settings['cols'], 0)  # Start with empty grid
    
    while True:
        print("\n=== Grid Editor ===")
        print("Current grid state:")
        print_grid(grid, 0)
        print("\nEditor Commands:")
        print("- Enter row and column numbers to toggle a cell")
        print("- Enter 'q' to finish editing")
        
        command = input("\nEnter command (row col or 'q'): ").strip().lower()
        
        if command == 'q':
            break
        
        try:
            row, col = map(int, command.split())
            if 0 <= row < settings['rows'] and 0 <= col < settings['cols']:
                grid = toggle_cell(grid, row, col)
            else:
                print(f"Coordinates must be within grid bounds (0-{settings['rows']-1}, 0-{settings['cols']-1})")
        except ValueError:
            print("Invalid input. Enter two numbers separated by space or 'q' to quit")
    
    return grid

def display_menu():
    """Display interactive menu for Conway's Game of Life."""
    # Default settings
    settings = {
        'rows': 20,
        'cols': 20,
        'alive_prob': 0.2,
        'interval': 0.1,
        'wrap': True,
        'steps': None
    }
    
    grid = None
    
    while True:
        print("\n=== Conway's Game of Life ===")
        print("\nCurrent Settings:")
        print(f"Grid Size: {settings['rows']}x{settings['cols']}")
        print(f"Initial Life Probability: {settings['alive_prob']}")
        print(f"Update Interval: {settings['interval']} seconds")
        print(f"Edge Wrapping: {'On' if settings['wrap'] else 'Off'}")
        
        print("\nOptions:")
        print("1. Start Simulation")
        print("2. Configure Grid Size")
        print("3. Set Initial Life Probability")
        print("4. Adjust Speed")
        print("5. Toggle Edge Wrapping")
        print("6. Edit Grid Manually")
        print("7. Reset Grid")
        print("8. Exit")
        
        if grid is not None:
            print("\nCurrent Grid State:")
            for row in grid:                                 
                print("".join('*' if cell else '.' for cell in row))
        
        choice = get_integer_input("\nEnter your choice (1-8): ", 1, 8)
        
        if choice == 1:
            # Start simulation
            steps = get_integer_input("Enter number of steps (0 for infinite): ", 0)
            settings['steps'] = None if steps == 0 else steps
            
            # If there's no existing grid, create one with the current settings
            if grid is None:
                grid = make_grid(settings['rows'], settings['cols'], settings['alive_prob'])
            
            # Pass the existing grid to run function
            grid = run(grid=grid, steps=settings['steps'], interval=settings['interval'], 
                      wrap=settings['wrap'])
            
        elif choice == 2:
            # Configure grid size
            print("\nConfigure Grid Size")
            settings['rows'] = get_integer_input("Enter number of rows (5-100): ", 5, 100)
            settings['cols'] = get_integer_input("Enter number of columns (5-100): ", 5, 100)
            grid = None  # Reset grid when size changes
            
        elif choice == 3:
            # Set initial life probability
            print("\nSet Initial Life Probability for New Grid")
            #if ther existing grid, warn user
            if grid is not None:
                confirm = input("Changing this will reset the current grid. Continue? (y/n): ").strip().lower()
                if confirm != 'y':
                    continue
            
            settings['alive_prob'] = get_float_input(
                "Enter probability (0.0-1.0): ", 0.0, 1.0)
            grid = None  # Reset grid when probability changes
            
        elif choice == 4:
            # Adjust speed
            print("\nAdjust Update Speed")
            settings['interval'] = get_float_input(
                "Enter interval in seconds (0.01-2.0): ", 0.01, 2.0)
            
        elif choice == 5:
            # Toggle wrapping
            settings['wrap'] = not settings['wrap']
            print(f"\nEdge wrapping turned {'on' if settings['wrap'] else 'off'}")
            
        elif choice == 6:
            # Edit grid manually
            if grid is None:
                grid = make_grid(settings['rows'], settings['cols'], 0)  # Start with empty grid
            grid = edit_grid(grid, settings)
            
        elif choice == 7:
            # Reset grid
            grid = None
            print("\nGrid reset. New grid will be generated when simulation starts.")
            
        elif choice == 8:
            # Exit
            print("\nThank you for playing Conway's Game of Life!")
            break


if __name__ == "__main__":
    try:
        display_menu()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    
