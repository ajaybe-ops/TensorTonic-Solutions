import numpy as np

def conv2d(X: list, W: list, b: list) -> np.ndarray:
    X = np.asarray(X, dtype=float)
    W = np.asarray(W, dtype=float)
    b = np.asarray(b, dtype=float)

    N, C_in, H, W_in = X.shape
    C_out, _, K_h, K_w = W.shape

    H_out = H - K_h + 1
    W_out = W_in - K_w + 1

    output = np.zeros((N, C_out, H_out, W_out))

    for n in range(N):
        for c_out in range(C_out):
            for i in range(H_out):
                for j in range(W_out):

                    total = b[c_out]

                    for c_in in range(C_in):
                        for kh in range(K_h):
                            for kw in range(K_w):
                                total += (
                                    X[n, c_in, i + kh, j + kw]
                                    * W[c_out, c_in, kh, kw]
                                )

                    output[n, c_out, i, j] = total

    return output