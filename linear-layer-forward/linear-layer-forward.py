import numpy as np 

def linear_layer_forward(X: list, W: list, b: list) ->list:
    X = np.asarray(X, dtype=float)
    W = np.asarray(W, dtype=float)
    b = np.asarray(b, dtype=float)

    return (X @ W + b).tolist()