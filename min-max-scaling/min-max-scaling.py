def min_max_scaling(data: list) -> list:
    rows = len(data)
    cols = len(data[0])

    result = [[0.0] * cols for _ in range(rows)]

    for j in range(cols):
        column = [data[i][j] for i in range(rows)]

        min_val = min(column)
        max_val = max(column)

        for i in range(rows):
            if max_val == min_val:
                result[i][j] = 0.0
            else:
                result[i][j] = (data[i][j] - min_val) / (max_val - min_val)

    return result