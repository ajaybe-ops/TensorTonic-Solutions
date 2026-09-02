def make_diagonal(v: list) -> np.ndarray:
    n = len(v)
    matrix = np.zeros((n, n))

    for i in range(n):
        matrix[i][i] = v[i]
    return matrix        