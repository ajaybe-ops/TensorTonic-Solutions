import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    v = np.array(v)

    if v.ndim == 1:
        return np.sqrt(np.sum(v ** 2))

    return np.sqrt(np.sum(v ** 2, axis=1))