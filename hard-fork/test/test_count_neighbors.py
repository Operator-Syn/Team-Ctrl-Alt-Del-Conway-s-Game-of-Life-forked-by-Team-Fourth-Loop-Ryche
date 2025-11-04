import pytest
from src.count_neighbors import count_neighbors

# Small visual helper for clarity
def make_grid(text):
    """Convert a multiline string of '.' and '*' into a grid of 0s and 1s."""
    lines = [line.strip() for line in text.strip().splitlines()]
    return [[1 if char == '*' else 0 for char in line] for line in lines]