import math

def cyclic_encoding(values: list, period: float) -> list:
    return [
        [math.sin(2 * math.pi * v / period),
         math.cos(2 * math.pi * v / period)]
        for v in values
    ]