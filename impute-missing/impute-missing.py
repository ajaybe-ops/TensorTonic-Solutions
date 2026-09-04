import numpy as np


def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    Missing values (NaN) are replaced using mean or median.
    """

    arr = np.array(X, dtype=float)

    is_1d = arr.ndim == 1

    if is_1d:
        arr = arr.reshape(-1, 1)

    result = arr.copy()

    for col in range(result.shape[1]):

        column = result[:, col]

        valid_values = column[~np.isnan(column)]

        if len(valid_values) == 0:
            fill_value = 0.0

        elif strategy == "mean":
            fill_value = np.mean(valid_values)

        elif strategy == "median":
            fill_value = np.median(valid_values)

        result[np.isnan(result[:, col]), col] = fill_value

    if is_1d:
        result = result.flatten()

    return result