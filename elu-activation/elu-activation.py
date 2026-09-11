import math

def elu(x: list, alpha: float = 1.0) -> list:
    result = []

    for value in x:
        if value > 0:
            result.append(value)
        else:
            result.append(alpha * (math.exp(value) - 1))

    return result