import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    A = np.array(A, dtype=float)
    n = len(A)

    # Augmenting A with the identity matrix
    augmented = np.hstack((A, np.eye(n)))

    for col in range(n):

        # Finding the best pivot row
        pivot_row = col + np.argmax(
            np.abs(augmented[col:, col])
        )

        # Matrix is singular
        if augmented[pivot_row, col] == 0:
            return None

        # Swap rows
        augmented[[col, pivot_row]] = augmented[
            [pivot_row, col]
        ]

        # Making pivot equal to 1
        augmented[col] = (
            augmented[col] / augmented[col, col]
        )

        # Eliminating this column from every other row
        for row in range(n):
            if row != col:
                augmented[row] -= (
                    augmented[row, col] * augmented[col]
                )

    # Returning the right half
    return augmented[:, n:]