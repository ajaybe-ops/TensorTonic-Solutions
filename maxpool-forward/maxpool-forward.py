def maxpool_forward(X: list, pool_size: int, stride: int) -> list:
    output = []

    rows = len(X)
    cols = len(X[0])

    for i in range(0, rows - pool_size + 1, stride):
        row = []

        for j in range(0, cols - pool_size + 1, stride):
            window = []

            for r in range(i, i + pool_size):
                for c in range(j, j + pool_size):
                    window.append(X[r][c])

            row.append(max(window))

        output.append(row)

    return output