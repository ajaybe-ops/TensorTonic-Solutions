import math

def he_initialization(W: list, fan_in: int) -> list:
    L = math.sqrt(6 / fan_in)

    result = []

    for row in W:
        new_row = []

        for w in row:
            new_w = w * 2 * L - L
            new_row.append(round(new_w, 4))

        result.append(new_row)

    return result