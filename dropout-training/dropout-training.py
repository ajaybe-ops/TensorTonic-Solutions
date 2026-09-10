import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None
) -> tuple[np.ndarray, np.ndarray]:

    x = np.asarray(x, dtype=float)

    keep_prob = 1 - p

    if rng is None:
        mask = np.random.random(x.shape) < keep_prob
    else:
        mask = rng.random(x.shape) < keep_prob

    dropout_pattern = mask.astype(float) / keep_prob

    output = x * dropout_pattern

    return output, dropout_pattern