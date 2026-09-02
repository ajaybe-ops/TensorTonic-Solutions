import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    A = np.array(matrix, dtype=float)
    eigenvalues = np.linalg.eigvals(A)
    return np.sort(eigenvalues.real)

print(calculate_eigenvalues([[4, 1], [2, 3]]))