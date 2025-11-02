import random

def make_grid(rows, cols, alive_prob=0.2):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if random.random() < alive_prob:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid
    #Code below is the original code before recent edits
    #return [[1 if random.random() < alive_prob else 0 for _ in range(cols)] for _ in range(rows)]
