import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """Return linearly interpolated percentiles."""
    
    x = sorted(x)
    n = len(x)
    result = []

    for percentile in q:
        r = percentile / 100 * (n - 1)

        l = int(np.floor(r))
        u = int(np.ceil(r))
        w = r - l

        value = (1 - w) * x[l] + w * x[u]
        result.append(value)

    return np.array(result)