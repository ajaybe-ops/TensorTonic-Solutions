def frequency_encoding(values: list) -> list:
    n = len(values)

    counts = {}

    for value in values:
        counts[value] = counts.get(value, 0) + 1

    return [counts[value] / n for value in values]