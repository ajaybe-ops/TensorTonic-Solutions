import math

def log_transform(values: list) -> list:
    return [round(math.log1p(x), 4) for x in values]