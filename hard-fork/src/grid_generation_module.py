import random

def make_grid(rows, cols, alive_prob=0.2):
    return [[1 if random.random() < alive_prob else 0 for _ in range(cols)] for _ in range(rows)]