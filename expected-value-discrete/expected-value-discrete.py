def expected_value_discrete(x: list, p: list) -> float:
    return float(sum(xi * pi for xi, pi in zip(x, p)))