import math

def selu(xs: list) -> list:
    lambda_ = 1.0507
    alpha = 1.6733

    result = []

    for x in xs:
        if x > 0:
            result.append(lambda_ * x)
        else:
            result.append(lambda_ * alpha * (math.exp(x) - 1))
            
    return [round(x, 4) for x in result]