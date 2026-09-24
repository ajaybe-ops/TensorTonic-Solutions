def binning(values: list, num_bins: int) -> list:
    if not values:
        return []

    minimum = min(values)
    maximum = max(values)

    #all wert getting identical gerade
    if minimum == maximum:
        return[0] * len(values)

    width = (maximum - minimum) / num_bins

    return [
        min(int((x - minimum) / width), num_bins - 1)
        for x in values
    ]