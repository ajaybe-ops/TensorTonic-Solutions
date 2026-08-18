import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """

    # Convert inputs to 2D
    x, x_was_1d = _as2d(x, params["Wz"].shape[0])
    h_prev, h_was_1d = _as2d(h_prev, params["Uz"].shape[0])

    # Update gate
    z = _sigmoid(
        x @ params["Wz"] +
        h_prev @ params["Uz"] +
        params["bz"]
    )

    # Reset gate
    r = _sigmoid(
        x @ params["Wr"] +
        h_prev @ params["Ur"] +
        params["br"]
    )

    # Candidate hidden state
    h_tilde = np.tanh(
        x @ params["Wh"] +
        (r * h_prev) @ params["Uh"] +
        params["bh"]
    )

    # Final hidden state
    h = (1 - z) * h_prev + z * h_tilde

    # Return 1D output if input was 1D
    if x_was_1d and h_was_1d:
        return h.reshape(-1)

    return h