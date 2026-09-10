import numpy as np

def global_avg_pool(x: list) -> np.ndarray:
    x = np.asarray(x, dtype=float)

    if x.ndim == 3:
        return np.mean(x, axis=(1, 2))
    else:
        return np.mean(x, axis=(2, 3))