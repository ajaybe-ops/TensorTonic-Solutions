import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Return the Manhattan distance between x and y.
    """
    return float(sum(abs(a - b) for a, b in zip(x, y)))
                      
    pass