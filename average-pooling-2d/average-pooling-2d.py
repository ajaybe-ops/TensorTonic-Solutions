
def average_pooling_2d(x: list, pool_size: int) -> list:
    result = []

    rows = len(x)
    cols = len(x[0])

    # Move through the input matrix
    for i in range(0, rows, pool_size):
        row = []

        for j in range(0, cols, pool_size):
            total = 0

            # Visit every element inside the pooling window
            for a in range(pool_size):
                for b in range(pool_size):
                    total += x[i + a][j + b]

            # Calculate the average
            average = total / (pool_size * pool_size)

            row.append(average)

        result.append(row)

    return result