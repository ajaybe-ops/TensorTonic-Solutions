def polynomial_features(values: list, degree: int) -> list:
    return [[x ** power for power in range(degree + 1)] for x in values]
    