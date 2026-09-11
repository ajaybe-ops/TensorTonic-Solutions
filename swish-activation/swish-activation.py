import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """

    # Convert input to a NumPy array with float type
    x_arr = np.asarray(x, dtype=np.float64)

    # Compute sigmoid safely
    sigmoid = np.where(
        x_arr >= 0,
        1.0 / (1.0 + np.exp(-x_arr)),
        np.exp(x_arr) / (1.0 + np.exp(x_arr))
    )

    # Return element-wise Swish
    return x_arr * sigmoid