import numpy as np

def rnn_step_backward(dh: list, cache: list) -> dict:
    x_t, h_prev, h_t, W, U, b = cache

    # Convert inputs to NumPy arrays
    dh = np.array(dh)
    x_t = np.array(x_t)
    h_prev = np.array(h_prev)
    h_t = np.array(h_t)
    W = np.array(W)
    U = np.array(U)

    # Gradient through tanh
    dz = dh * (1 - h_t ** 2)

    # Gradients
    dx_t = W.T @ dz
    dh_prev = U.T @ dz
    dW = np.outer(dz, x_t)
    dU = np.outer(dz, h_prev)
    db = dz

    # Return NumPy arrays, NOT lists
    return {
        "dx_t": dx_t,
        "dh_prev": dh_prev,
        "dW": dW,
        "dU": dU,
        "db": db
    }