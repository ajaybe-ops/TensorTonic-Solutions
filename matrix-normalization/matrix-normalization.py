import numpy as np


def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    
    matrix = np.array(matrix, dtype=float)

    if norm_type == "l1":
        norm = np.sum(np.abs(matrix), axis=axis, keepdims=(axis is not None))

    elif norm_type == "l2":
        norm = np.sqrt(np.sum(matrix ** 2, axis=axis, keepdims=(axis is not None)))

    elif norm_type == "max":
        norm = np.max(np.abs(matrix), axis=axis, keepdims=(axis is not None))

    else:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")

    return np.divide(
        matrix,
        norm,
        out=np.zeros_like(matrix),
        where=(norm != 0)
    )