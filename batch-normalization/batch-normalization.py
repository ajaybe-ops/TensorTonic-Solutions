import numpy as np

def batch_norm_forward(x: list, gamma: list, beta: list, eps: float = 1e-5) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    beta = np.asarray(beta, dtype=float)

    # Channel dimension is axis 1
    axes = tuple(i for i in range(x.ndim) if i != 1)

    mean = np.mean(x, axis=axes, keepdims=True)
    variance = np.var(x, axis=axes, keepdims=True)

    x_norm = (x - mean) / np.sqrt(variance + eps)

    # Reshape gamma/beta so they broadcast across N, H, W
    shape = [1] * x.ndim
    shape[1] = len(gamma)

    gamma = gamma.reshape(shape)
    beta = beta.reshape(shape)

    return gamma * x_norm + beta